from config import config_utilities
from services.utilities_services import suggest_utilities, support_utilities, complaint_utilities, collab_utilities, appointment_utilities
from fastapi import APIRouter, Depends, HTTPException, Path, Query
from models import request_dto, utilities

# Initialize Router
router = APIRouter()
utilities_collection = config_utilities()

@router.post("/suggest")
async def suggest_utilities_req(request: request_dto):
    res_text = await suggest_utilities()
    return {"original_text": request.text, "processed_text": res_text}

@router.post("/support")
async def support_utilities_req(request: request_dto):
    res_text = await support_utilities()
    return {"original_text": request.text, "processed_text": res_text}

@router.post("/complaint")
async def complaint_utilities_req(request: request_dto):
    res_text = await complaint_utilities()
    return {"original_text": request.text, "processed_text": res_text}

@router.post("/collab")
async def collab_utilities_req(request: request_dto):
    res_text = await collab_utilities()
    return {"original_text": request.text, "processed_text": res_text}

@router.post("/appointment")
async def appointment_utilities_req(request: request_dto):
    res_text = await appointment_utilities()
    return {"original_text": request.text, "processed_text": res_text}