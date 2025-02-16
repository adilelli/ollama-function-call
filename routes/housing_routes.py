from config import *
from services.housing_services import suggest_housing, support_housing, complaint_housing, collab_housing, appointment_housing
from fastapi import APIRouter, Depends, HTTPException, Path, Query
from models import request_dto, housing

# Initialize Router
router = APIRouter()
housing_collection = config_housing()

@router.post("/suggest")
async def suggest_housing_req(request: request_dto):
    res_text = await suggest_housing()
    return {"original_text": request.text, "processed_text": res_text}

@router.post("/support")
async def support_housing_req(request: request_dto):
    res_text = await support_housing()
    return {"original_text": request.text, "processed_text": res_text}

@router.post("/complaint")
async def complaint_housing_req(request: request_dto):
    res_text = await complaint_housing()
    return {"original_text": request.text, "processed_text": res_text}

@router.post("/collab")
async def collab_housing_req(request: request_dto):
    res_text = await collab_housing()
    return {"original_text": request.text, "processed_text": res_text}

@router.post("/appointment")
async def appointment_housing_req(request: request_dto):
    res_text = await appointment_housing()
    return {"original_text": request.text, "processed_text": res_text}