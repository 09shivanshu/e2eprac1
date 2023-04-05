import pymongo
import pandas as pd
import json
from datatclass import dataclasss
import os


# Provide the mongodb localhost url to connect python to mongodb.
@dataclasss
class EnviromentVariable():
    mongo_db_url:str = os.getenv("MONGO_DB_URL")

env_var = EnviromentVariable()
mongo_client = pymongo.MongoClient(env_var.mongo_db_url)



