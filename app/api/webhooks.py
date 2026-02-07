from fastapi import APIRouter, Request

router = APIRouter()

@router.post("/{endpoint_id}")
async def receive_webhook(endpoint_id: str, request: Request):
    payload = await request.json()
    print("Received webhook for endpoint:", endpoint_id)
    print("Payload:", payload)
    
    return {"status": "success"}