from config import *
from services.transport_services import suggest_transport, support_transport, complaint_transport, collab_transport, appointment_transport
from fastapi import APIRouter, Depends, HTTPException, Path, Query
from models import request_dto, transport

# Initialize Router
router = APIRouter()
transport_collection = config_transport()

@router.post("/suggest")
async def suggest_transport_req(request: request_dto):
    res_text = await suggest_transport()
    return {"original_text": request.text, "processed_text": res_text}

@router.post("/support")
async def support_transport_req(request: request_dto):
    res_text = await support_transport()
    return {"original_text": request.text, "processed_text": res_text}

@router.post("/complaint")
async def complaint_transport_req(request: request_dto):
    res_text = await complaint_transport()
    return {"original_text": request.text, "processed_text": res_text}

@router.post("/collab")
async def collab_transport_req(request: request_dto):
    res_text = await collab_transport()
    return {"original_text": request.text, "processed_text": res_text}

@router.post("/appointment")
async def appointment_transport_req(request: request_dto):
    res_text = await appointment_transport()
    return {"original_text": request.text, "processed_text": res_text}