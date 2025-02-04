from config import config_attraction
from services.attraction_services import suggest_attraction, support_attraction, complaint_attraction, collab_attraction, appointment_attraction
from fastapi import APIRouter, Depends, HTTPException, Path, Query
from models import request_dto, attraction

# Initialize Router
router = APIRouter()
attraction_collection = config_attraction()

@router.post("/suggest_attraction")
async def suggest_attraction(request: request_dto):
    processed_text = request.text.upper()  # Example processing: convert text to uppercase
    await suggest_attraction()
    return {"original_text": request.text, "processed_text": processed_text}