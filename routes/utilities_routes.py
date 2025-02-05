from config import config_utilities
from services.utilities_services import suggest_utilities, support_utilities, complaint_utilities, collab_utilities, appointment_utilities
from fastapi import APIRouter, Depends, HTTPException, Path, Query
from models import request_dto, utilities

# Initialize Router
router = APIRouter()
utilities_collection = config_utilities()

@router.post("/suggest_utilities")
async def suggest_utilities_req(request: request_dto):
    res_text = await suggest_utilities()
    return {"original_text": request.text, "processed_text": res_text}

@router.post("/support_utilities")
async def support_utilities_req(request: request_dto):
    res_text = await support_utilities()
    return {"original_text": request.text, "processed_text": res_text}

@router.post("/complaint_utilities")
async def complaint_utilities_req(request: request_dto):
    res_text = await complaint_utilities()
    return {"original_text": request.text, "processed_text": res_text}

@router.post("/collab_utilities")
async def collab_utilities_req(request: request_dto):
    res_text = await collab_utilities()
    return {"original_text": request.text, "processed_text": res_text}

@router.post("/appointment_utilities")
async def appointment_utilities_req(request: request_dto):
    res_text = await appointment_utilities()
    return {"original_text": request.text, "processed_text": res_text}