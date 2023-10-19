from pymongo import  MongoClient

client = MongoClient("localhost:27017")
db = client["BornToWin_shop"]

users_col = db["Users"]
mice_col = db["Mice"]
keyboards_col = db["Keyboards"]
headphones_col = db["Headphones"]
speakers_col = db["Speakers"]
mousepads_col = db["Mousepads"]
orders_col = db["Orders"]