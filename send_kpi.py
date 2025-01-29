import json
import requests

SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/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"

# Load KPI data
with open("daily_kpi.json", "r") as file:
    kpi = json.load(file)

# Format message
message = f"""
*{kpi['date']} - Daily KPI Info*

*Business Stats (Onboarding)*
• New Visitors: *{kpi['new_visitors']}* (<percent> more/less than previous visitors)
• New Signups: *{kpi['new_signups']}* (<percent> of visitors) (<percent> more/less than previous signups)
• Signups that placed a demo call for the first time: *{kpi['first_time_demo']}* (<percent> of signups) (<percent> more/less than previous demo calls)
• Total Demo calls placed: *{kpi['total_demo_calls']}* (<percent> more/less than previous total demo calls)
• Subscriptions cancelled: *{kpi['subscriptions']['canceled']}*
• New subscriptions: *{kpi['subscriptions']['new']}* (<percent> of signups) (<percent> of signups that placed demo calls)
• Current total active subscriptions: *{kpi['subscriptions']['active']}* (No change from previous subscriptions)

*Call Stats*
• Total campaign calls: *{kpi['call_stats']['total']}* (<percent> more/less than previous campaign calls)
• Calls placed without errors: *{kpi['call_stats']['without_errors']}* (<percent> of campaign calls)
• Calls connected: *{kpi['call_stats']['connected']}* (<percent> of calls placed without errors)
• Calls Duration longer than 29 sec: *{kpi['call_stats']['long_duration']}* (<percent> of calls connected)
• Average Assistant response time: *{kpi['avg_response_time']}s* (<percent> more/less than previous average)
"""

# Send to Slack
response = requests.post(SLACK_WEBHOOK_URL, json={"text": message})

# Check for successful Slack webhook execution
if response.status_code == 200:
    print("KPI report sent to Slack successfully!")
else:
    print(f"Failed to send report to Slack. Status code: {response.status_code}")
