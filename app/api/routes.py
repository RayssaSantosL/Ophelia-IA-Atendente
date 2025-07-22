from fastapi import APIRouter, Request, Response, HTTPException
import os

router = APIRouter()

VERIFY_TOKEN = os.getenv("VERIFY_TOKEN", "ophelia5202")

@router.get("/webhook")
async def verify_webhook(request: Request):
    params = dict(request.query_params)
    if params.get("hub.mode") == "subscribe" and params.get("hub.verify_token") == VERIFY_TOKEN:
        challenge = params.get("hub.challenge")
        return Response(content=challenge)
    else:
        raise HTTPException(status_code=403, detail="Verification token mismatch")
