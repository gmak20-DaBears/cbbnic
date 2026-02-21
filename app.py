import streamlit as st
import random
import requests

# 1. Configuration
CHANNEL_ID = "1163193122244505600"
# WARNING: Keep this token secret! Don't share your URL with strangers.
USER_TOKEN = "YOUR_SLEEPER_TOKEN_HERE" 

def get_latest_sleeper_comment():
    url = f"https://sleeper.com/api/v1/channel/{CHANNEL_ID}/messages?limit=1"
    headers = {"authorization": USER_TOKEN}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            msg_data = response.json()
            if msg_data:
                return msg_data[0]['text'], msg_data[0].get('display_name', 'User')
        return "Could not fetch message", "System"
    except:
        return "Connection Error", "System"

# Data for Wrestlers & Teams
WRESTLERS = [
    {"name": "Stone Cold Steve Austin", "image": "https://upload.wikimedia.org/wikipedia/commons/e/e0/Stone_Cold_Steve_Austin.jpg"},
    {"name": "Ric Flair", "image": "https://www.wwe.com/f/all/2017/02/Ric_Flair_pro--f6e2e388909890f5555.jpg"}
]
NCAAB_TEAMS = [
    {"name": "Duke Blue Devils", "logo": "https://upload.wikimedia.org/wikipedia/commons/0/04/Duke_Blue_Devils_logo.svg"},
    {"name": "Kentucky Wildcats", "logo": "https://upload.wikimedia.org/wikipedia/commons/5/5d/Kentucky_Wildcats_logo.svg"}
]

st.title("🏀 Auto-Sleeper Legend Match")

if st.button("Fetch Last Comment & Match"):
    comment_text, username = get_latest_sleeper_comment()
    
    wrestler = random.choice(WRESTLERS)
    team = random.choice(NCAAB_TEAMS)

    st.subheader(f"Latest from {username}:")
    st.info(comment_text)
    
    col1, col2 = st.columns(2)
    with col1:
        st.header(wrestler['name'])
        st.image(wrestler['image'])
    with col2:
        st.header(team['name'])
        st.image(team['logo'])
