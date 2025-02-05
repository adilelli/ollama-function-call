from config import config_attraction
from services.attraction_services import suggest_attraction, support_attraction, complaint_attraction, collab_attraction, appointment_attraction
from fastapi import APIRouter, Depends, HTTPException, Path, Query
from models import request_dto, attraction

# Initialize Router
router = APIRouter()
attraction_collection = config_attraction()

@router.post("/suggest_attraction")
async def suggest_attraction_req(request: request_dto):
    res_text = suggest_attraction()
    return {"original_text": request.text, "processed_text": res_text}

@router.post("/support_attraction")
async def support_attraction_req(request: request_dto):
    res_text = await support_attraction()
    return {"original_text": request.text, "processed_text": res_text}

@router.post("/complaint_attraction")
async def complaint_attraction_req(request: request_dto):
    res_text = await complaint_attraction()
    return {"original_text": request.text, "processed_text": res_text}

@router.post("/collab_attraction")
async def collab_attraction_req(request: request_dto):
    res_text = await collab_attraction()
    return {"original_text": request.text, "processed_text": res_text}

@router.post("/appointment_attraction")
async def appointment_attraction_req(request: request_dto):
    res_text = await appointment_attraction()
    return {"original_text": request.text, "processed_text": res_text}