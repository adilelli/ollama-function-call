from config import *
from services.healthcare_services import suggest_healthcare, support_healthcare, complaint_healthcare, collab_healthcare, appointment_healthcare
from fastapi import APIRouter, Depends, HTTPException, Path, Query
from models import request_dto, healthcare

# Initialize Router
router = APIRouter()
healthcare_collection = config_healthcare()

@router.post("/suggest")
async def suggest_healthcare_req(request: request_dto):
    res_text = await suggest_healthcare()
    return {"original_text": request.text, "processed_text": res_text}

@router.post("/support")
async def support_healthcare_req(request: request_dto):
    res_text = await support_healthcare()
    return {"original_text": request.text, "processed_text": res_text}

@router.post("/complaint")
async def complaint_healthcare_req(request: request_dto):
    res_text = await complaint_healthcare()
    return {"original_text": request.text, "processed_text": res_text}

@router.post("/collab")
async def collab_healthcare_req(request: request_dto):
    res_text = await collab_healthcare()
    return {"original_text": request.text, "processed_text": res_text}

@router.post("/appointment")
async def appointment_healthcare_req(request: request_dto):
    res_text = await appointment_healthcare()
    return {"original_text": request.text, "processed_text": res_text}