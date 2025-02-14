import string
import ollama
from pydantic import BaseModel

# class CallResponse(BaseModel):
#     tool: any
#     response: any

def add_numbers(a: int, b: int) -> int:
    """
    Add two numbers

    Args:
      a: The first integer number
      b: The second integer number

    Returns:
      int: The sum of the two numbers
    """
    print(f"add_two_numbers called with a={a}, b={b}")  # Debug print
    return a + b

def multiply_numbers(a: int, b: int) -> int:
    """
    Add two numbers

    Args:
      a: The first integer number
      b: The second integer number

    Returns:
      int: The sum of the two numbers
    """
    print(f"Multiply_two_numbers called with a={a}, b={b}")  # Debug print
    return a * b

print("Calling ollama.chat...")  # Debug print


print("ollama.chat response received.")  # Debug print
print("Checking tool calls...")  # Debug print

available_functions = {
    'add_numbers': add_numbers,
    'multiply_numbers': multiply_numbers,
}

def functionCall(request: str, model: str):
    try:
        response = ollama.chat(
            model,
            messages=[{'role': 'user', 'content': request}],
            tools=[add_numbers, multiply_numbers],  # Actual function reference
        )
        return response.message
    except Exception as e:
        print(f"Error in functionCall: {e}")  # Log the error
        return None  # Return None or handle the error appropriately

    # for tool in response.message.tool_calls or []:
    #     print(f"Processing tool call: {tool.function.name}")  # Debug print
    #     function_to_call = available_functions.get(tool.function.name)
    #     if function_to_call:
    #         print(f"Executing function: {tool.function.name}")  # Debug print
    #         response = function_to_call(**tool.function.arguments)
    #         print('Function output:', response)
    #         return tool
    #     else:
    #         print('Function not found:', tool.function.name)


from langchain_ollama import OllamaLLM
from pydantic import BaseModel

class Country(BaseModel):
    name: str
    capital: str
    languages: list[str]

def get_country_info(country_name: str) -> Country:
    llm = OllamaLLM(model="llama3.1")  # Load Ollama model

    response = llm.invoke(
        f"Tell me about {country_name}.",
    )

    return Country.model_validate_json(response)

# Example usage
country_info = get_country_info("Canada")
print(country_info)

