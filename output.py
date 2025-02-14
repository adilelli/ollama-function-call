from fastapi import FastAPI
from pydantic import BaseModel
import os
import json
from mistralai import Mistral

# Set API Key
os.environ["MISTRAL_API_KEY"] = "cIRC6j2aIOKKTSqqsVxsKx5A0314Wtwt"

# Initialize FastAPI & Mistral Client
app = FastAPI()
client = Mistral(api_key=os.getenv("MISTRAL_API_KEY"))
model = "mistral-large-latest"

# Define Pydantic Model for the request body
class ChatRequest(BaseModel):
    prompt: str

# Define Pydantic Model for function parameters
class WeatherRequest(BaseModel):
    city: str

class Book(BaseModel):
    name: str
    authors: list[str]

# Mock function to return weather data
def get_weather(city: str):
    return {
        "city": city,
        "temperature": 25.5,
        "condition": "Sunny"
    }

# Define available functions
functions = [
    {
        "name": "get_weather",
        "description": "Fetch the current weather for a given city.",
        "parameters": WeatherRequest.schema()
    }
]
tools = [
     {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Fetch the current weather for a given city.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The location",
                    }
                },
                "required": ["location"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "retrieve_payment_status",
            "description": "Get payment status of a transaction",
            "parameters": {
                "type": "object",
                "properties": {
                    "transaction_id": {
                        "type": "string",
                        "description": "The transaction id.",
                    }
                },
                "required": ["transaction_id"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "retrieve_payment_date",
            "description": "Get payment date of a transaction",
            "parameters": {
                "type": "object",
                "properties": {
                    "transaction_id": {
                        "type": "string",
                        "description": "The transaction id.",
                    }
                },
                "required": ["transaction_id"],
            },
        },
    }
]

# API Endpoint to interact with Mistral
@app.post("/output")
async def structured_output_mistral(request: ChatRequest):  # Accept JSON body
    response = client.chat.parse(
        model=model,
        messages=[
            {
                "role": "system", 
                "content": "Extract the books information."
            },
            {
                "role": "user", 
                "content": request.prompt
            },
        ],
        response_format=Book,
        max_tokens=256,
        temperature=0
    )

    return {"response": response}  # Default text response