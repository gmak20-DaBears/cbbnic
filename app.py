import streamlit as st
import random
import requests

# --- 1. CONFIGURATION ---
# Replace the TOKEN below if it expires (from your Network tab)
TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOiI2MTE0MjIwODY2OTQ3NjA0NDgiLCJkaXNwbGF5TmFtZSI6IkNoaUJlYXJzODQiLCJhdmF0YXIiOiJlZTRhM2VmMzY4ZGJlYzc3ZmJhOTA4ZDgxNWZiZDI4NyIsInNsZWVwZXJUb2tlbiI6ImV5SmhiR2NpT2lKSVV6STFOaUlzSW5SNWNDSTZJa3BYVkNKOS5leUpoZG1GMFlYSWlPaUpsWlRSaE0yVm1Nelk0WkdKbFl6YzNabUpoT1RBNFpEZ3hOV1ppWkRJNE55SXNJbVJwYzNCc1lYbGZibUZ0WlNJNklrTm9hVUpsWVhKek9EUWlMQ0psZUhBaU9qRTNPRGt3TVRJNU9UZ3NJbWxoZENJNk1UYzFOelEzTmprNU9Dd2lhWE5mWW05MElqcG1ZV3h6WlN3aWFYTmZiV0Z6ZEdWeUlqcG1ZV3h6WlN3aWNtVmhiRjl1WVcxbElqcHVkV3hzTENKMWMyVnlYMmxrSWpvMk1URTBNakl3T0RZMk9UUTNOakEwTkRnc0luWmhiR2xrWHpKbVlTSTZJbkJvYjI1bEluMC5FOGR3eUVfMGMtUFNoaEcxaWVoUDBwaTRhNUVWU2RFUUtxVG03LUh1a0dVIiwiZW1haWwiOiJnbWFrMjBAeWFob28uY29tIiwidHlwZSI6InNlc3Npb24iLCJpYXQiOjE3NzE2ODAwODcsImV4cCI6MTgwMzIxNjA4NywiaXNzIjoic2xlZXBlci13ZWIiLCJhdWQiOiJzbGVlcGVyLXdlYiJ9.Z6VfZzIZ-NVZFynOieVAhagnNtdhvwADbaYUND7LBbg"
CID = "1163193122244505600"

def get_msg():
    url = f"https://api.sleeper.app/v1/channel/{CID}/messages?limit=1"
    headers = {"Authorization": TOKEN, "User-Agent": "Mozilla/5.0"}
    try:
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            d = r.json()
            if d:
                return d[0]['text'], d[0].get('display_name', 'User')
    except:
        pass
    return None, None

# --- 2. IMAGE DATA (Verified Links) ---
WRESTLERS = [
    {"name": "Stone Cold Steve Austin", "url": "https://i.imgur.com/3vK9uIu.jpg"},
    {"name": "Ric Flair", "url": "https://i.imgur.com/WfR2fM0.jpg"},
    {"name": "Hulk Hogan", "url": "https://i.imgur.com/86D3mC4.jpg"}
]

TEAMS = [
    {"name": "Duke Blue Devils", "url": "https://i.imgur.com/vH9v5mX.png"},
    {"name": "Kentucky Wildcats", "url": "https://i.imgur.com/pYxV0eK.png"},
    {"name": "Kansas Jayhawks", "url": "https://i.imgur.com/uG5h1H1.png"}
]

# --- 3. USER INTERFACE ---
st.set_page_config(page_title="Sleeper Matcher", layout="wide")
st.title("🤼‍♂️ Sleeper Legend Matcher")

if st.button("Fetch & Match!"):
    # 1. Fetch data
    msg_text, msg_user = get_msg()
    
    # 2. Pick random items
    wrestler = random.choice(WRESTLERS)
    team = random.choice(TEAMS)
    
    # 3. Display message section
    if msg_text:
        st.subheader(f"Latest from: {msg_user}")
        st.info(msg_text)
    else:
        st.warning("Could not fetch message from Sleeper (Token expired). Showing match only:")

    # 4. Display images in two columns
    col1, col2 = st.columns(2)
    
    with col1:
        st.header(wrestler["name"])
        st.image(wrestler["url"], use_container_width=True)
        
    with col2:
        st.header(team["name"])
        st.image(team["url"], use_container_width=True)
