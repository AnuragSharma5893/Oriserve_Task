# Oriserve_Task

# objective 

This project automates the generation and reporting of daily KPIs for VoiceGenie. The KPIs include data related to user activity, call sessions, subscriptions, and other relevant metrics, which are extracted from a MongoDB database. The data is then formatted into a Slack-compatible message and sent to a Slack channel for easy tracking and reporting.

## **Features**

- **Data Collection:** Fetches KPIs from MongoDB collections for users, subscriptions, and call sessions.
- **KPI Generation:** Generates KPIs for:
  - New Visitors
  - New Signups
  - First-time Demo Calls
  - Total Demo Calls
  - Subscriptions (New, Canceled, Active)
  - Call Statistics (Total, Connected, Without Errors, Calls > 29 sec)
  - Average Assistant Response Time
- **Slack Integration:** Sends the generated KPIs as a formatted message to a Slack channel.
- **Automation:** Automates the entire process through a Python script and cron job for daily execution.

## **Installation**

### **1. Set Up MongoDB**
Ensure that you have a local or remote MongoDB instance running and populate it with the necessary collections and data. You can use the provided `setup_db.py` script to insert dummy data into MongoDB.

### **2. Install Dependencies**
Install the required Python packages using pip:

```bash
pip install pymongo slack_sdk
```

### **3. MongoDB Database Setup**
To set up the MongoDB collections with dummy data, run the `setup_db.py` script:

```bash
python setup_db.py
```

This will populate the `users`, `subscriptions`, and `CallSessionHistories` collections with sample data.

### **4. Slack Webhook Setup**
Set up a Slack webhook by creating an incoming webhook in your Slack workspace. Replace `YOUR_SLACK_WEBHOOK_URL` in the `send_kpi.py` script with your actual webhook URL.

---

## **Usage**

### **1. Generate KPIs**
To generate KPIs, run the following command:

```bash
python generate_kpi.py
```

This script will fetch the required data from MongoDB, compute the KPIs, and save them into a `daily_kpi.json` file.

### **2. Send KPIs to Slack**
After generating the KPIs, you can send the report to Slack by running:

```bash
python send_kpi.py
```

This will post the formatted KPI data to the specified Slack channel.

---

## **Automating the Process**

To automate the daily execution of the KPI generation and reporting, you can set up a cron job. For example, to run the process every day at 9 AM, add the following entry to your crontab:

```bash
0 9 * * * python /path/to/generate_kpi.py && python /path/to/send_kpi.py
```

Alternatively, you can create a custom bash alias to run the process manually:

```bash
echo "alias vg-kpi='python /path/to/generate_kpi.py && python /path/to/send_kpi.py'" >> ~/.bashrc
source ~/.bashrc
```

After this, you can run the process with the command:

```bash
vg-kpi
```

---

## **File Structure**

```
/project-root
│
├── setup_db.py           # Script to set up dummy data in MongoDB
├── generate_kpi.py       # Script to generate daily KPIs
├── send_kpi.py           # Script to send KPIs to Slack
├── daily_kpi.json        # File to store generated KPI data
└── README.md             # Project documentation
```
