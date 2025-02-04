from config import config_food
from services.attraction_services import suggest_attraction, support_attraction, complaint_attraction, collab_attraction, appointment_attraction
from fastapi import APIRouter, Depends, HTTPException, Path, Query
from models import request_dto, attraction

# Initialize Router
router = APIRouter()
food_collection = config_food()