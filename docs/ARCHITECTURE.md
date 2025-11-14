# Architecture — BuzzGuard (MVP)

## High level components
- Scrapers (snscrape, RSS / newspaper3k)
- Ingestion (simple HTTP POST to worker or direct DB insert)
- Worker: enrichment (sentiment + embeddings)
- DB: MongoDB (text index)
- Backend: FastAPI exposing REST + WS (optional)
- Frontend: React (Vite) showing feed + charts
- Deployment: Vercel (frontend) + Render/Railway (backend) + MongoDB Atlas

## Data model (unified mention)
- mention_id, source, url, text, author, published_at, collected_at, sentiment{label,score}, topics[], embedding[]

## Spike detection
- time-windowed counts + z-score detection, produce alert when z > threshold

## Tradeoffs
- Use snscrape to avoid API keys but for production use official APIs
- Hugging Face local pipelines for no cost, OpenAI for speed
