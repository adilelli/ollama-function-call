from config import *
from services.infra_services import suggest_infra, support_infra, complaint_infra, collab_infra, appointment_infra
from fastapi import APIRouter, Depends, HTTPException, Path, Query
from models import request_dto, infra

# Initialize Router
router = APIRouter()
infra_collection = config_infra()

@router.post("/suggest_infra")
async def suggest_infra_req(request: request_dto):
    res_text = await suggest_infra()
    return {"original_text": request.text, "processed_text": res_text}

@router.post("/support_infra")
async def support_infra_req(request: request_dto):
    res_text = await support_infra()
    return {"original_text": request.text, "processed_text": res_text}

@router.post("/complaint_infra")
async def complaint_infra_req(request: request_dto):
    res_text = await complaint_infra()
    return {"original_text": request.text, "processed_text": res_text}

@router.post("/collab_infra")
async def collab_infra_req(request: request_dto):
    res_text = await collab_infra()
    return {"original_text": request.text, "processed_text": res_text}

@router.post("/appointment_infra")
async def appointment_infra_req(request: request_dto):
    res_text = await appointment_infra()
    return {"original_text": request.text, "processed_text": res_text}