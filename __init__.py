import os
from pymongo import MongoClient
from dotenv import load_dotenv

APP_ROOT = os.path.join(os.path.dirname(__file__), '')   # refers to application_top
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)
from space import *

mongo_url = os.getenv('MONGO_URL')
client = MongoClient(mongo_url)
db = client['villagecontent']
