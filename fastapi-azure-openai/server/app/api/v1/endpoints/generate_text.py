from fastapi import APIRouter, HTTPException
from app.models.request import TextRequest
from app.services.openai_service import generate_openai_text

router = APIRouter()

@router.post("/generate-text/")
async def generate_text(request: TextRequest):
    response = generate_openai_text(request.prompt)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()
