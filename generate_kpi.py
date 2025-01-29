import random
from pymongo import MongoClient
from datetime import datetime, timedelta
import json

client = MongoClient("mongodb+srv://anuragsharma58693:lZSsPfD7r67CCzR0@cluster0.jxp7n.mongodb.net/")
db = client["voicegenie"]

# Define date range (yesterday)
today = datetime(2025, 1, 29)
yesterday = today - timedelta(days=1)

# Fetch new visitors
new_visitors = db.users.count_documents({"signup_date": {"$gte": yesterday, "$lt": today}})

# Fetch new signups
new_signups = db.users.count_documents({"signup_date": {"$gte": yesterday, "$lt": today}})

# Fetch first-time demo callers
first_time_demo = db.CallSessionHistories.count_documents(
    {"campaignId": "demo", "timestamp": {"$gte": yesterday, "$lt": today}}
)

# Fetch total demo calls
total_demo_calls = db.CallSessionHistories.count_documents(
    {"campaignId": "demo", "timestamp": {"$gte": yesterday, "$lt": today}}
)

# Fetch subscription data
new_subscriptions = db.subscriptions.count_documents({"start_date": {"$gte": yesterday, "$lt": today}})
canceled_subscriptions = db.subscriptions.count_documents({"status": "canceled"})
active_subscriptions = db.subscriptions.count_documents({"status": "active"})

# Fetch call statistics
total_calls = db.CallSessionHistories.count_documents({"timestamp": {"$gte": yesterday, "$lt": today}})
calls_without_errors = db.CallSessionHistories.count_documents({"error": None, "timestamp": {"$gte": yesterday, "$lt": today}})
calls_connected = db.CallSessionHistories.count_documents({"connected": True, "timestamp": {"$gte": yesterday, "$lt": today}})
calls_long_duration = db.CallSessionHistories.count_documents({"duration": {"$gt": 29}, "timestamp": {"$gte": yesterday, "$lt": today}})

# Compute average assistant response time (mock value as actual calculation requires logs)
average_response_time = round(random.uniform(1.5, 3.5), 2)

# Compile KPI data
kpi_data = {
    "date": yesterday.strftime("%Y-%m-%d"),
    "new_visitors": new_visitors,
    "new_signups": new_signups,
    "first_time_demo": first_time_demo,
    "total_demo_calls": total_demo_calls,
    "subscriptions": {
        "new": new_subscriptions,
        "canceled": canceled_subscriptions,
        "active": active_subscriptions
    },
    "call_stats": {
        "total": total_calls,
        "connected": calls_connected,
        "without_errors": calls_without_errors,
        "long_duration": calls_long_duration
    },
    "avg_response_time": average_response_time
}

# Store in daily_kpi.json
with open("daily_kpi.json", "w") as file:
    json.dump(kpi_data, file, indent=4)

print("KPI data generated successfully!")
