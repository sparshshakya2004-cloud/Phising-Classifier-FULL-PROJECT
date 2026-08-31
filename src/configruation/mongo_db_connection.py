# import os
# import sys

# import certifi
# import pymongo

# from src.constant import *
# from src.exception import CustomException

# ca = certifi.where()


# class MongoDBClient:
#     client = None

#     def __init__(self, database_name=MONGO_DATABASE_NAME) -> None:
#         try:
#             if MongoDBClient.client is None:
#                 mongo_db_url = os.getenv("MONGO_DB_URL")
#                 if mongo_db_url is None:
#                     raise Exception("Environment key: MONGO_DB_URL is not set.")
#                 MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
#             self.client = MongoDBClient.client
#             self.database = self.client[database_name]
#             self.database_name = database_name
#         except Exception as e:
#             raise CustomException(e, sys)


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