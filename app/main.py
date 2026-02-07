from fastapi import FastAPI
from app.api.webhooks import router as webhook_router   

app = FastAPI(title="Webhook Tester")

app.include_router(webhook_router, prefix="/hooks")