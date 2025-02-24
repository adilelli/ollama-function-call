from config import config_food
from services.food_services import suggest_food, support_food, complaint_food, collab_food, appointment_food
from fastapi import APIRouter, Depends, HTTPException, Path, Query
from models import request_dto, food

# Initialize Router
router = APIRouter()
food_collection = config_food()

@router.post("/suggest")
async def suggest_food_req(request: request_dto):
    res_text = await suggest_food()
    return {"original_text": request.text, "processed_text": res_text}

@router.post("/support")
async def support_food_req(request: request_dto):
    res_text = await support_food()
    return {"original_text": request.text, "processed_text": res_text}

@router.post("/complaint")
async def complaint_food_req(request: request_dto):
    res_text = await complaint_food()
    return {"original_text": request.text, "processed_text": res_text}

@router.post("/collab")
async def collab_food_req(request: request_dto):
    res_text = await collab_food()
    return {"original_text": request.text, "processed_text": res_text}

@router.post("/appointment")
async def appointment_food_req(request: request_dto):
    res_text = await appointment_food()
    return {"original_text": request.text, "processed_text": res_text}