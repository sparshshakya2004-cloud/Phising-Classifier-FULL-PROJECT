import os
from urllib.parse import quote_plus

from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.server_api import ServerApi
# from src.constant import *

load_dotenv()

username = quote_plus(os.environ["MONGO_USERNAME"])
password = quote_plus(os.environ["MONGO_PASSWORD"])
host = os.environ["MONGO_HOST"]
database_name = os.environ["MONGO_DATABASE"]

uri = f"mongodb+srv://{username}:{password}@{host}/?retryWrites=true&w=majority"

client = MongoClient(uri, server_api=ServerApi("1"))
database = client[database_name]

try:
    client.admin.command("ping")
    print("Successfully connected to MongoDB!")
except Exception as error:
    print(f"MongoDB connection failed: {error}")

    