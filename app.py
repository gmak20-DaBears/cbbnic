import streamlit as st
import random
import requests

# --- 1. SETTINGS ---
# Replace the text below with your actual token from the Network tab
USER_TOKEN = "YOUR_ACTUAL_TOKEN_HERE"
CHANNEL_ID = "1163193122244505600"

def get_sleeper_data():
    # This is the direct pipe to your specific chat
    url = f"https://sleeper.com/api/v1/channel/{CHANNEL_ID}/messages?limit=1"
    headers = {
        "Authorization": USER_TOKEN,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    try:
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            data = r.json()
            if data:
                return data[0]['text'], data[0].get('display_name', 'User')
            return "No messages found.", "System"
        return f"Error {r.status_code}", "System"
    except:
        return "Connection Error", "System"

# --- 2. DATA (Stable Wikipedia Links) ---
WRESTLERS = [
    {"n": "Stone Cold", "i": "https://upload.wikimedia.org/wikipedia/commons/e/e0/Stone_Cold_Steve_Austin.jpg"},
    {"n": "Ric Flair", "i": "https://upload.wikimedia.org/wikipedia/commons/1/13/Ric_Flair_July_2016.jpg"},
    {"n": "Hulk Hogan", "i": "https://upload.wikimedia.org/wikipedia/commons/4/4b/Hulk_Hogan_July_2015.jpg"}
]

TEAMS = [
    {"n": "Duke", "l": "https://upload.wikimedia.org/wikipedia/commons/0/04/Duke_Blue_Devils_logo.svg"},
    {"n": "Kentucky", "l": "https://upload.wikimedia.org/wikipedia/commons/5/5d/Kentucky_Wildcats_logo.svg"},
    {"n": "Kansas", "l": "https://upload.wikimedia.org/wikipedia/en/9/9e/Kansas_Jayhawks_logo.svg"}
]

# --- 3. THE WEBSITE UI ---
st.set_page_config(page_title="Sleeper Legend Match", layout="wide")
st.title("🏀 Sleeper Legend Matcher")

if st.button("Fetch Last Comment & Match!"):
    text, user = get_sleeper_data()
    w = random.choice(WRESTLERS)
    t = random.choice(TEAMS)

    st.subheader(f"Latest from: {user}")
    st.info(text)
    
    col1, col2 = st.columns(2)
    with col1:
        st.header(w['n'])
        st.image(w['i'], use_container_width=True)
    with col2:
        st.header(t['n'])
        st.image(t['l'], use_container_width=True)
