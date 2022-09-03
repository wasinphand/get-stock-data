import pymongo
import os
import dotenv
from typing import List
import helper

dotenv.load_dotenv()
USERNAME = os.getenv("USERNAME") or ""
PASSWORD = os.getenv("PASSWORD") or ""
CLUSTER_NAME = os.getenv("CLUSTER_NAME") or ""

url = "mongodb+srv://{USERNAME}:{PASSWORD}@{CLUSTER_NAME}.mongodb.net/?retryWrites=true&w=majority".format(USERNAME=USERNAME,PASSWORD=PASSWORD,CLUSTER_NAME=CLUSTER_NAME)
cluster = pymongo.MongoClient(host=url)
db = cluster["Stock-Historical-Data"]

def createDividendData(search:str, data:dict):
    collection = db[search]
    response = collection.insert_one(data)
    return response.inserted_id

def createDelistedEquitiesData(search:str, data:List[dict]):
    collection = db[search]
    response = collection.insert_many(data)
    return response.inserted_ids