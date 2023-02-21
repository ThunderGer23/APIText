# Connecting to the MongoDB database.
from pymongo import MongoClient
from os import environ

conn = MongoClient(environ['MONGO_CLI'])