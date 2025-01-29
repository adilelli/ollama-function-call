import os
from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from pydantic import BaseModel
from bson import ObjectId

from llama import add_numbers, functionCall, multiply_numbers

# Initialize FastAPI app
app = FastAPI()

# MongoDB Atlas connection
MONGO_URI = os.environ.get("MONGO_URI")  # Replace with your MongoDB Atlas URI
client = MongoClient(MONGO_URI)
db = client["llama"]  # Replace with your database name
collection = db["admin"]  # Replace with your collection name

# Pydantic model for request/response validation
class Item(BaseModel):
    name: str
    description: str
    price: float
    in_stock: bool

class Action(BaseModel):
    name: str
    a: int
    b: int


# Helper function to convert MongoDB ObjectId to string
def convert_objectid_to_str(item):
    item["_id"] = str(item["_id"])
    return item

# GET all items
@app.get("/call")
async def get_function_call(request: str = None, model: str = None):
    if not request or not model:
        raise HTTPException(status_code=400, detail="Either request or model is empty")
    tool = functionCall(request, model)
    if not tool:
        raise HTTPException(status_code=400, detail=f"Model {model} does not support function")
    return tool

# Function mapping
available_functions = {
    "add_numbers": add_numbers,
    "multiply_numbers": multiply_numbers,
}


@app.post("/execute_call")
async def execute_call(action: Action):
    if not action.name:
        raise HTTPException(status_code=400, detail="Empty execution request")

    # Get function from the dictionary
    function_to_call = available_functions.get(action.name)
    if not function_to_call:
        raise HTTPException(status_code=400, detail="Function not found")

    # Call the function with the provided data
    return function_to_call(action.a,action.b)

# GET all items
@app.get("/items")
def get_all_items():
    items = list(collection.find())
    return [convert_objectid_to_str(item) for item in items]

# GET a single item by ID
@app.get("/items/{item_id}")
def get_item(item_id: str):
    item = collection.find_one({"_id": ObjectId(item_id)})
    if item:
        return convert_objectid_to_str(item)
    else:
        raise HTTPException(status_code=404, detail="Item not found")

# POST a new item
@app.post("/items")
def create_item(item: Item):
    item_dict = item.model_dump()
    result = collection.insert_one(item_dict)
    return {"id": str(result.inserted_id)}

# PUT (update) an item by ID
@app.put("/items/{item_id}")
def update_item(item_id: str, item: Item):
    item_dict = item.model_dump()
    result = collection.update_one({"_id": ObjectId(item_id)}, {"$set": item_dict})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item updated successfully"}

# DELETE an item by ID
@app.delete("/items/{item_id}")
def delete_item(item_id: str):
    result = collection.delete_one({"_id": ObjectId(item_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted successfully"}