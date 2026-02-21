import streamlit as st
import random
import requests

# --- 1. SETTINGS ---
# This is your specific session token found in the cookie data
USER_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOiI2MTE0MjIwODY2OTQ3NjA0NDgiLCJkaXNwbGF5TmFtZSI6IkNoaUJlYXJzODQiLCJhdmF0YXIiOiJlZTRhM2VmMzY4ZGJlYzc3ZmJhOTA4ZDgxNWZiZDI4NyIsInNsZWVwZXJUb2tlbiI6ImV5SmhiR2NpT2lKSVV6STFOaUlzSW5SNWNDSTZJa3BYVkNKOS5leUpoZG1GMFlYSWlPaUpsWlRSaE0yVm1Nelk0WkdKbFl6YzNabUpoT1RBNFpEZ3hOV1ppWkRJNE55SXNJbVJwYzNCc1lYbGZibUZ0WlNJNklrTm9hVUpsWVhKek9EUWlMQ0psZUhBaU9qRTNPRGt3TVRJNU9UZ3NJbWxoZENJNk1UYzFOelEzTmprNU9Dd2lhWE5mWW05MElqcG1ZV3h6WlN3aWFYTmZiV0Z6ZEdWeUlqcG1ZV3h6WlN3aWNtVmhiRjl1WVcxbElqcHVkV3hzTENKMWMyVnlYMmxrSWpvMk1URTBNakl3T0RZMk9UUTNOakEwTkRnc0luWmhiR2xrWHpKbVlTSTZJbkJvYjI1bEluMC5FOGR3eUVfMGMtUFNoaEcxaWVoUDBwaTRhNUVWU2RFUUtxVG03LUh1a0dVIiwiZW1haWwiOiJnbWFrMjBAeWFob28uY29tIiwidHlwZSI6InNlc3Npb24iLCJpYXQiOjE3NzE2ODAwODcsImV4cCI6MTgwMzIxNjA4NywiaXNzIjoic2xlZXBlci13ZWIiLCJhdWQiOiJzbGVlcGVyLXdlYiJ9.Z6VfZzIZ-NVZFynOieVAhagnNtdhvwADbaYUND7LBbg"
CHANNEL_ID = "1163193122244505600"

def get_sleeper_data():
    # Attempting to fetch from the specific channel
    url = f"https://api.sleeper.app/v1/channel/{CHANNEL_ID}/messages?limit=1"
    headers = {
        "Authorization": USER_TOKEN,
        "User-Agent": "Mozilla/5.0"
    }
    try:
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            data = r.json()
            if data and len(data) > 0:
                return data[0]['text'], data[0].get('display_name', 'User')
        return None, None
    except:
        return None, None

# --- 2. DATA (Stable Links) ---
WRESTLERS = [
    {"n": "Stone Cold", "i": "https://i.imgur.com/3vK9uIu.jpg"},
    {"n": "Ric Flair", "i": "https://i.imgur.com/WfR2fM0.jpg"},
    {"n": "Hulk Hogan", "i": "https://i.imgur.com/86D3mC4.jpg"}
]

TEAMS = [
    {"n": "Duke", "l": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Duke_Blue_Devils_logo.svg/1200px-Duke_Blue_Devils_logo.svg.png"},
    {"n": "Kentucky", "l": "https://upload.wikimedia
