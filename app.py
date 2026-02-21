import streamlit as st
import random
import requests

# --- 1. ACCESS KEYS ---
# FRESH TOKEN NEEDED: Get from Browser -> Inspect -> Network -> 'authorization'
TK = "eyJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOiI2MTE0MjIwODY2OTQ3NjA0NDgiLCJkaXNwbGF5TmFtZSI6IkNoaUJlYXJzODQiLCJhdmF0YXIiOiJlZTRhM2VmMzY4ZGJlYzc3ZmJhOTA4ZDgxNWZiZDI4NyIsInNsZWVwZXJUb2tlbiI6ImV5SmhiR2NpT2lKSVV6STFOaUlzSW5SNWNDSTZJa3BYVkNKOS5leUpoZG1GMFlYSWlPaUpsWlRSaE0yVm1Nelk0WkdKbFl6YzNabUpoT1RBNFpEZ3hOV1ppWkRJNE55SXNJbVJwYzNCc1lYbGZibUZ0WlNJNklrTm9hVUpsWVhKek9EUWlMQ0psZUhBaU9qRTNPRGt3TVRJNU9UZ3NJbWxoZENJNk1UYzFOelEzTmprNU9Dd2lhWE5mWW05MElqcG1ZV3h6WlN3aWFYTmZiV0Z6ZEdWeUlqcG1ZV3h6WlN3aWNtVmhiRjl1WVcxbElqcHVkV3hzTENKMWMyVnlYMmxrSWpvMk1URTBNakl3T0RZMk9UUTNOakEwTkRnc0luWmhiR2xrWHpKbVlTSTZJbkJvYjI1bEluMC5FOGR3eUVfMGMtUFNoaEcxaWVoUDBwaTRhNUVWU2RFUUtxVG03LUh1a0dVIiwiZW1haWwiOiJnbWFrMjBAeWFob28uY29tIiwidHlwZSI6InNlc3Npb24iLCJpYXQiOjE3NzE2ODAwODcsImV4cCI6MTgwMzIxNjA4NywiaXNzIjoic2xlZXBlci13ZWIiLCJhdWQiOiJzbGVlcGVyLXdlYiJ9.Z6VfZzIZ-NVZFynOieVAhagnNtdhvwADbaYUND7LBbg"
ID = "1163193122244505600"

def get_latest_comment():
    # This endpoint reaches into the specific side-chat channel
    url = f"https://api.sleeper.app/v1/channel/{ID}/messages?limit=1"
    
    headers = {
        "Authorization": TK,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Referer": "https://sleeper.com/",
        "Origin": "https://sleeper.com",
        "Accept": "application/json"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if data and len(data) > 0:
                # Returns: The Text, The Sender's Name, and Status 200
                return data[0]['text'], data[0].get('display_name', 'Unknown User'), 200
            return "No messages in this chat yet.", "System", 200
        return None, None, response.status_code
    except Exception as e:
        return None, None, str(e)

# --- 2. THE BIG LISTS ---
WRESTLERS = [
    {"n": "Stone Cold", "i": "https://i.ibb.co/XfXkMDR/stone-cold.jpg"},
    {"n": "Ric Flair", "i": "https://i.ibb.co/0Ym7K7z/ric-flair.jpg"},
    {"n": "Hulk Hogan", "i": "https://i.ibb.co/hR4y5Nn/hulk-hogan.jpg"},
    {"n": "The Rock", "i": "https://upload.wikimedia.org/wikipedia/commons/1/11/Dwayne_Johnson_2021.jpg"},
    {"n": "John Cena", "i": "https://upload.wikimedia.org/wikipedia/commons/6/60/John_Cena_July_2018.jpg"}
]

COLLEGES = [
    {"n": "Duke", "l": "https://a.espncdn.com/i/teamlogos/ncaa/500/150.png"},
    {"n": "Kentucky", "l": "https://a.espncdn.com/i/teamlogos/ncaa/500/96.png"},
    {"n": "Kansas", "l": "https://a.espncdn.com/i/teamlogos/ncaa/500/2305.png"},
    {"n": "UConn", "l": "https://a.espncdn.com/i/teamlogos/ncaa/500/41.png"},
    {"n": "North Carolina", "l": "https://a.espncdn.com/i/teamlogos/ncaa/500/153.png"},
    {"n": "Michigan State", "l": "https://a.espncdn.com/i/teamlogos/ncaa/500/127.png"}
]

# --- 3. UI DISPLAY ---
st.set_page_config(page_title="Sleeper Side-Chat Matcher", layout="wide")
st.title("🚀 Sleeper Side-Chat Matcher")

if st.button("GET LATEST MESSAGE & MATCH", use_container_width=True):
    msg, sender, status = get_latest_comment()
    wrestler = random.choice(WRESTLERS)
    college = random.choice(COLLEGES)
    
    if status == 200:
        st.success(f"✅ Successfully fetched message from **{sender}**")
        st.markdown(
