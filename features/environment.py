# environment.py
import requests
import os

def before_all(context):
    context.base_url = os.getenv("BASE_URL", "http://127.0.0.1:8000")

def before_scenario(context, scenario):
    # Сбрасываем БД перед каждым сценарием
    requests.delete(f"{context.base_url}/reset")