from pymongo import MongoClient
from datetime import datetime, timedelta
import random

client = MongoClient("mongodb+srv://anuragsharma58693:lZSsPfD7r67CCzR0@cluster0.jxp7n.mongodb.net/")
db = client["voicegenie"]

# Clear collections if they exist
db.users.drop()
db.subscriptions.drop()
db.CallSessionHistories.drop()

# Generate dummy user data
users = [
    {"user_id": i, "signup_date": datetime(2025, 1, 28) if i % 3 == 0 else datetime(2025, 1, 27)}
    for i in range(100)
]

# Generate dummy subscription data
subscriptions = [
    {"user_id": i, "status": random.choice(["active", "canceled"]), "start_date": datetime(2025, 1, 25)}
    for i in range(20)
]

# Generate dummy call session history
call_sessions = [
    {
        "call_id": i,
        "user_id": random.randint(1, 100),
        "campaignId": "demo" if i % 2 == 0 else "campaign",
        "duration": random.randint(10, 50),
        "error": None if i % 5 != 0 else "Some Error",
        "connected": i % 3 == 0,
        "timestamp": datetime(2025, 1, 28)
    }
    for i in range(200)
]

# Insert into database
db.users.insert_many(users)
db.subscriptions.insert_many(subscriptions)
db.CallSessionHistories.insert_many(call_sessions)

print("Dummy data inserted successfully!")
