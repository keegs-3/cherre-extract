# src/cherre_api.py

import requests
from src.auth import get_auth_headers

CHERRE_URL = "https://graphql.cherre.com/graphql"

def run_query(query, variables=None):
    headers = get_auth_headers()
    payload = {
        "query": query,
        "variables": variables or {}
    }

    response = requests.post(CHERRE_URL, json=payload, headers=headers)
    if not response.ok:
        raise Exception(f"❌ API Error {response.status_code}: {response.text}")
    
    return response.json()

