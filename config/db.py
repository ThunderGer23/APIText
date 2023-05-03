# Connecting to the MongoDB database.
from pymongo import MongoClient
from config.keys import MongoCli

conn = MongoClient("mongodb://mongo:w9nv2Uj41vovywuLLfV3@containers-us-west-190.railway.app:5921")
