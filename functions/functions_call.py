import ollama
from services.attraction_services import suggest_attraction, support_attraction, complaint_attraction, collab_attraction, appointment_attraction
from services.education_services import suggest_education, support_education, complaint_education, collab_education, appointment_education
from services.healthcare_services import suggest_healthcare, support_healthcare, complaint_healthcare, collab_healthcare, appointment_healthcare
from services.housing_services import suggest_housing, support_housing, complaint_housing, collab_housing, appointment_housing
from services.transport_services import suggest_transport, support_transport, complaint_transport, collab_transport, appointment_transport
from services.infra_services import suggest_infra, support_infra, complaint_infra, collab_infra, appointment_infra
from services.food_services import suggest_food, support_food, complaint_food, collab_food, appointment_food

from pydantic import BaseModel

class ResponseModel(BaseModel):
    location: str
    date: str
    name: str

def functionCall(request: str, model: str):
    try:
        response = ollama.chat(
            model,
            messages=[{'role': 'user', 'content': request}],
            tools=[
                suggest_attraction, support_attraction, complaint_attraction, collab_attraction, appointment_attraction,
                suggest_education, support_education, complaint_education, collab_education, appointment_education,
                suggest_healthcare, support_healthcare, complaint_healthcare, collab_healthcare, appointment_healthcare,
                suggest_housing, support_housing, complaint_housing, collab_housing, appointment_housing,
                suggest_transport, support_transport, complaint_transport, collab_transport, appointment_transport,
                suggest_infra, support_infra, complaint_infra, collab_infra, appointment_infra,
                suggest_food, support_food, complaint_food, collab_food, appointment_food
            ],
            # format=ResponseModel.model_json_schema(),
        )
        return response.message
    except Exception as e:
        print(f"Error in functionCall: {e}")  # Log the error
        return None  # Return None or handle the error appropriately

def get_country_info(country_name: str) -> ResponseModel:
    response = ollama.chat(
        messages=[
            {
                'role': 'user',
                'content': f'Tell me about {country_name}.',
            }
        ],
        model='llama3.1',
        format=ResponseModel.model_json_schema(),
    )

    return ResponseModel.model_validate_json(response.message.content)

# Example usage
country_info = get_country_info("Canada")
print(country_info)
