# PRD — BuzzGuard (MVP)

## Problem statement
Marketing teams miss critical mentions across multiple channels. BuzzGuard provides real-time aggregation, sentiment detection, topic clustering, and spike alerts.

## Goal
Deliver a deployable MVP that:
- Ingests mentions from X (snscrape) and News (RSS) / Reddit
- Runs sentiment analysis
- Stores mentions
- Presents a dashboard with live feed + basic analytics + spike alerts

## MVP Features
- Scrapers: X, News
- Enrichment: sentiment (HF pipeline or OpenAI)
- Storage: MongoDB Atlas
- API: /api/mentions
- Frontend: Live feed, sentiment chart, spike alert

## Success metrics
- Live demo link
- End-to-end pipeline working
- Spike alert demonstrable in demo
