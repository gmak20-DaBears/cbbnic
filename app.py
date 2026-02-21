import streamlit as st
import random
import requests

# --- CONFIGURATION ---
CHANNEL_ID = "1163193122244505600"
# PASTE YOUR TOKEN BELOW
USER_TOKEN = "YOUR_ACTUAL_TOKEN_HERE" 

def get_latest_sleeper_comment():
    url = f"https://sleeper.com/api/v1/channel/{CHANNEL_ID}/messages?limit=1"
    headers = {"Authorization": USER_TOKEN, "User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            msg_data = response.json()
            if msg_data:
                return msg_data[0]['text'], msg_data[0].get('display_name', 'User')
            return "No messages found.", "System"
        return f"Error {response.status_code}", "System"
    except:
        return "Connection Error", "System"

# --- DATA ---
WRESTLERS = [
    {"name": "Stone Cold", "image": "https://upload.wikimedia.org/wikipedia/commons/e/e0/Stone_Cold_Steve_Austin.jpg"},
    {"name": "Ric Flair", "image": "https://upload.wikimedia.org/wikipedia/commons/1/13/Ric_Flair_July_2016.jpg"},
    {"name": "Hulk Hogan", "image": "https://upload.wikimedia.org/wikipedia/commons/4/4b/Hulk_Hogan_July_2015.jpg"}
]

NCAAB_TEAMS = [
    {"name": "Duke", "logo": "https://upload.wikimedia.org/wikipedia/commons/0/04/Duke_Blue_Devils_logo.svg"},
    {"name": "Kentucky", "logo": "https://upload.wikimedia.org/wikipedia/commons/5/5d/Kentucky_Wildcats_logo.svg"},
    {"name": "Kansas", "logo": "https://upload.wikimedia.org/wikipedia/en/9/9e/Kansas_Jayhawks_logo.svg"}
]

# --- APP INTERFACE ---
st.set_page_config(page_title="Sleeper Match", layout="wide")
st.title("🏀 Sleeper Legend Match")

if st.button("Fetch & Match!"):
    comment_text, username = get_latest_sleeper_comment()
    wrestler = random.choice(WRESTLERS)
    team = random.choice(NCAAB_TEAMS)

    st.subheader(f"Latest from {username}:")
    st.info(comment_text)
    
    col1, col2 = st.columns(2)
    with col1:
        st.header(w
