import requests

def trigger_n8n(data):
    webhook_url = "http://localhost:5678/webhook/grant-alert"
    requests.post(webhook_url, json=data)