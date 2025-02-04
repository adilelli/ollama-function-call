from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.attraction_routes import router as attraction_router
from routes.education_routes import router as education_router
from routes.food_routes import router as food_router
from routes.healthcare_routes import router as healthcare_router
from routes.housing_routes import router as housing_router
from routes.infra_routes import router as infra_router
from routes.transport_routes import router as transport_router
from routes.utilities_routes import router as utilities_router

app = FastAPI()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(attraction_router, prefix="/attraction")
app.include_router(education_router, prefix="/education")
app.include_router(food_router, prefix="/food")
app.include_router(healthcare_router, prefix="/healthcare")
app.include_router(housing_router, prefix="/housing")
app.include_router(infra_router, prefix="/infra")
app.include_router(transport_router, prefix="/transport")
app.include_router(utilities_router, prefix="/utilities")

@app.get("/", tags=["Root"])
async def root():
    return {"ok": "cool"}