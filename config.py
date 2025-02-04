import os
from dotenv import load_dotenv
from pymongo import MongoClient


load_dotenv()
def config_attraction():
    MONGO_URI = os.environ.get("MONGO_URI")
    client = MongoClient(MONGO_URI)
    db = client['fses']
    user = db['attraction']
    return user

def config_education():
    MONGO_URI = os.environ.get("MONGO_URI")
    client = MongoClient(MONGO_URI)
    db = client['fses']
    user = db['education']
    return user

def config_food():
    MONGO_URI = os.environ.get("MONGO_URI")
    client = MongoClient(MONGO_URI)
    db = client['fses']
    user = db['food']
    return user

def config_healthcare():
    MONGO_URI = os.environ.get("MONGO_URI")
    client = MongoClient(MONGO_URI)
    db = client['fses']
    user = db['healthcare']
    return user

def config_housing():
    MONGO_URI = os.environ.get("MONGO_URI")
    client = MongoClient(MONGO_URI)
    db = client['fses']
    user = db['housing']
    return user

def config_infra():
    MONGO_URI = os.environ.get("MONGO_URI")
    client = MongoClient(MONGO_URI)
    db = client['fses']
    user = db['infra']
    return user

def config_transport():
    MONGO_URI = os.environ.get("MONGO_URI")
    client = MongoClient(MONGO_URI)
    db = client['fses']
    user = db['transport']
    return user

def config_utilities():
    MONGO_URI = os.environ.get("MONGO_URI")
    client = MongoClient(MONGO_URI)
    db = client['fses']
    user = db['utilities']
    return user