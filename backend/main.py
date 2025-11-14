# backend/main.py
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import os
from pymongo import MongoClient

app = FastAPI(title="BuzzGuard API")

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
db = MongoClient(MONGO_URI).buzzguard

class MentionIn(BaseModel):
    mention_id: str
    source: str
    url: str = None
    text: str
    author: dict = None
    published_at: str = None

@app.post("/api/mentions")
async def ingest(mention: MentionIn):
    doc = mention.dict()
    doc["collected_at"] = datetime.utcnow().isoformat() + "Z"
    db.mentions.insert_one(doc)
    return {"status":"ok", "id": str(doc.get("mention_id"))}

@app.get("/api/mentions")
async def list_mentions(limit: int = 50):
    cursor = db.mentions.find().sort("collected_at", -1).limit(limit)
    return {"mentions": [ {k:v for k,v in m.items() if k != "_id"} for m in cursor ]}
