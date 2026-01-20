import json
import os
import requests

AKS_BASE_URL = os.environ.get("AKS_BASE_URL")

def lambda_handler(event, context):
    body = json.loads(event.get("body", "{}"))
    user_id = body.get("user_id")

    if not user_id:
        return response(400, {"error": "user_id is required"})

    r = requests.get(f"{AKS_BASE_URL}/users/{user_id}", timeout=3)
    return response(r.status_code, r.json())

def response(status, body):
    return {
        "statusCode": status,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body)
    }
