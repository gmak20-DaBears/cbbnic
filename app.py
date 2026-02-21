import streamlit as st
import random
import requests

# --- 1. PASTE YOUR DATA HERE ---
# Paste the link the Console gave you inside these quotes:
TARGET_URL = "https://sleeper.com/api/v1/channel/1163193122244505600/messages?limit=1"
# Paste your long authorization string here:
USER_TOKEN = "YOUR_ACTUAL_TOKEN_HERE"

def fetch_last_comment():
    headers = {
        "Authorization": USER_TOKEN,
        "User-Agent": "Mozilla/5.0"
    }
    try:
        r = requests.get(TARGET_URL, headers=headers)
        if r.status_code == 200:
            data = r.json()
            if data and len(data) > 0:
                # Returns the text and the person who said it
                return data[0]['text'], data[0].get('display_name', 'User')
        return f"Error {r.status_code}: Access Denied", "System"
    except:
        return "Connection failed", "System"

# --- 2. DATA ---
WRESTLERS = [
    {"n": "Stone Cold", "i": "https://upload.wikimedia.org/wikipedia/commons/e/e0/Stone_Cold_Steve_Austin.jpg"},
    {"n": "Ric Flair", "i": "https://upload.wikimedia.org/wikipedia/commons/1/13/Ric_Flair_July_2016.jpg"}
]

TEAMS = [
    {"n": "Duke", "l": "https://upload.wikimedia.org/wikipedia/commons/0/04/Duke_Blue_Devils_logo.svg"},
    {"n": "Kentucky", "l": "https://upload.wikimedia.org/wikipedia/commons/5/5d/Kentucky_Wildcats_logo.svg"}
]

# --- 3. UI ---
st.set_page_config(page_title="Sleeper Auto-Match", layout="wide")
st.title("🏀 Auto-Sleeper Matcher")

if st.button("Get Latest Chat Message"):
    comment, user = fetch_last_comment()
    w = random.choice(WRESTLERS)
    t = random.choice(TEAMS)

    st.subheader(f"Message from {user}:")
    st.info(comment)
    
    col1, col2 = st.columns(2)
    with col1:
        st.header(w['n'])
        st.image(w['i'], use_container_width=True)
    with col2:
        st.header(t['n'])
        st.image(t['l'], use_container_width=True)
