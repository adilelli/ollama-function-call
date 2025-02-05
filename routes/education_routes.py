from config import config_education
from services.education_services import suggest_education, support_education, complaint_education, collab_education, appointment_education
from fastapi import APIRouter, Depends, HTTPException, Path, Query
from models import request_dto, education

# Initialize Router
router = APIRouter()
education_collection = config_education()

@router.post("/suggest_education")
async def suggest_education_req(request: request_dto):
    res_text = await suggest_education()
    return {"original_text": request.text, "processed_text": res_text}

@router.post("/support_education")
async def support_education_req(request: request_dto):
    res_text = await support_education()
    return {"original_text": request.text, "processed_text": res_text}

@router.post("/complaint_education")
async def complaint_education_req(request: request_dto):
    res_text = await complaint_education()
    return {"original_text": request.text, "processed_text": res_text}

@router.post("/collab_education")
async def collab_education_req(request: request_dto):
    res_text = await collab_education()
    return {"original_text": request.text, "processed_text": res_text}

@router.post("/appointment_education")
async def appointment_education_req(request: request_dto):
    res_text = await appointment_education()
    return {"original_text": request.text, "processed_text": res_text}