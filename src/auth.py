# src/auth.py

import os
from dotenv import load_dotenv

load_dotenv()

def get_auth_headers():
    token = os.getenv("CHERRE_API_KEY")
    if not token:
        raise ValueError("❌ Missing CHERRE_API_KEY in .env")
    
    return {
        "Authorization": token,
        "Content-Type": "application/json"
    }

