import streamlit as st
import random
import requests

# --- SETTINGS ---
TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOiI2MTE0MjIwODY2OTQ3NjA0NDgiLCJkaXNwbGF5TmFtZSI6IkNoaUJlYXJzODQiLCJhdmF0YXIiOiJlZTRhM2VmMzY4ZGJlYzc3ZmJhOTA4ZDgxNWZiZDI4NyIsInNsZWVwZXJUb2tlbiI6ImV5SmhiR2NpT2lKSVV6STFOaUlzSW5SNWNDSTZJa3BYVkNKOS5leUpoZG1GMFlYSWlPaUpsWlRSaE0yVm1Nelk0WkdKbFl6YzNabUpoT1RBNFpEZ3hOV1ppWkRJNE55SXNJbVJwYzNCc1lYbGZibUZ0WlNJNklrTm9hVUpsWVhKek9EUWlMQ0psZUhBaU9qRTNPRGt3TVRJNU9UZ3NJbWxoZENJNk1UYzFOelEzTmprNU9Dd2lhWE5mWW05MElqcG1ZV3h6WlN3aWFYTmZiV0Z6ZEdWeUlqcG1ZV3h6WlN3aWNtVmhiRjl1WVcxbElqcHVkV3hzTENKMWMyVnlYMmxrSWpvMk1URTBNakl3T0RZMk9UUTNOakEwTkRnc0luWmhiR2xrWHpKbVlTSTZJbkJvYjI1bEluMC5FOGR3eUVfMGMtUFNoaEcxaWVoUDBwaTRhNUVWU2RFUUtxVG03LUh1a0dVIiwiZW1haWwiOiJnbWFrMjBAeWFob28uY29tIiwidHlwZSI6InNlc3Npb24iLCJpYXQiOjE3NzE2ODAwODcsImV4cCI6MTgwMzIxNjA4NywiaXNzIjoic2xlZXBlci13ZWIiLCJhdWQiOiJzbGVlcGVyLXdlYiJ9.Z6VfZzIZ-NVZFynOieVAhagnNtdhvwADbaYUND7LBbg"
CID = "1163193122244505600"

def get_msg():
    url = f"https://api.sleeper.app/v1/channel/{CID}/messages?limit=1"
    headers = {"Authorization": TOKEN, "User-Agent": "Mozilla/5.0"}
    try:
        r = requests.get(url, headers=headers, timeout=5)
        if r.status_code == 200:
            d = r.json()
            if d: return d[0]['text'], d[0].get('display_name', 'User')
    except: pass
    return None, None

# --- DATA (Using direct Wikimedia/Stable links) ---
WRESTLERS = [
    {"n": "Stone Cold", "i": "https://upload.wikimedia.org/wikipedia/commons/e/e0/Stone_Cold_Steve_Austin.jpg"},
    {"n": "Ric Flair", "i": "https://upload.wikimedia.org/wikipedia/commons/1/13/Ric_Flair_July_2016.jpg"},
    {"n": "Hulk Hogan", "i": "https://upload.wikimedia.org/wikipedia/commons/4/4b/Hulk_Hogan_July_2015.jpg"}
]

TEAMS = [
    {"n": "Duke", "l": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Duke_Blue_Devils_logo.svg/800px-Duke_Blue_Devils_logo.svg.png"},
    {"n": "Kentucky", "l": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Kentucky_Wildcats_logo.svg/800px-Kentucky_Wildcats_logo.svg.png"},
    {"n": "Kansas", "l": "https://upload.wikimedia.org/wikipedia/en/thumb/9/9e/Kansas_Jayhawks_logo.svg/800px-Kansas_Jayhawks_logo.svg.png"}
]

# --- UI ---
st.set_page_config(page_title="Sleeper Matcher", layout="centered")
st.title("🤼‍♂️ Sleeper Legend Matcher")

if st.button("Fetch & Match!"):
    txt, usr = get_msg()
    w, t = random.choice(WRESTLERS), random.choice(TEAMS)
    
    if txt:
        st.subheader(f"Latest from: {usr}")
        st.info(txt)
    else:
        st.warning("Message fetch failed (Token likely expired).")
    
    col1, col2 = st.columns(2)
    with col1:
        st.header(w['n'])
        st.image(w['i'], use_container_width=True)
    with col2:
        st.header(t['n'])
        st.image(t['l'], use_container_width=True)
