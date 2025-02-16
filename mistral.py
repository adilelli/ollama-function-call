from fastapi import FastAPI
from pydantic import BaseModel
import os
import json
from mistralai import Mistral

# Initialize FastAPI & Mistral Client
app = FastAPI()
client = Mistral(api_key=os.getenv("MISTRAL_API_KEY"))

# Define Pydantic Model for the request body
class ChatRequest(BaseModel):
    prompt: str

class Weather(BaseModel):
    city: str
    temperature: str

# Mock function to return weather data
# def get_weather(city: str):
#     return {
#         "city": city,
#         "temperature": 25.5,
#         "condition": "Sunny"
#     }

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
                        "type": "array",
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
@app.post("/chat")
async def chat_with_mistral(request: ChatRequest):  # Accept JSON body
    responseFunc = client.chat.complete(
        model="mistral-large-latest",
        messages=[{"role": "user", "content": request.prompt}],
        tools=tools,
        tool_choice = "any",
    )

    # # Check if Mistral wants to call a function
    # function_call = response.choices[0].message.function_call
    # if function_call:
    #     function_name = function_call.name
    #     arguments = json.loads(function_call.arguments)
        
    #     # if function_name == "get_weather":
    #     #     return get_weather(**arguments)  # Call our function

    responseObj = client.chat.parse(
        model="mistral-large-latest",
        messages=[
            {
                "role": "system", 
                "content": "Extract the weather information."
            },
            {
                "role": "user", 
                "content": request.prompt
            },
        ],
        response_format=Weather,
        max_tokens=256,
        temperature=0
    )

    return {"response_function": responseFunc, "response_structure": responseObj}  # Default text response