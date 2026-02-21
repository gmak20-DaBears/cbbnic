import streamlit as st
import random
import requests

# --- CONFIGURATION ---
CHANNEL_ID = "1163193122244505600"
# PASTE YOUR TOKEN HERE. It should be a long string of letters/numbers.
USER_TOKEN = "YOUR_ACTUAL_TOKEN_HERE" 

def get_latest_sleeper_comment():
    # Note: Sleeper often uses this specific internal URL for chat messages
    url = f"https://sleeper.com/api/v1/channel/{CHANNEL_ID}/messages?limit=1"
    headers = {
        "Authorization": USER_TOKEN,
        "User-Agent": "Mozilla/5.0" # Pretends to be a browser to avoid blocks
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            msg_data = response.json()
            if msg_data and len(msg_data) > 0:
                return msg_data[0]['text'], msg_data[0].get('display_name', 'Sleeper User')
            return "No messages found in this channel.", "System"
        elif response.status_code == 401:
            return "Error 401: Your Token is invalid or expired.", "System"
        else:
            return f"Error {response.status_code}: Could not reach Sleeper.", "System"
    except Exception as e:
        return f"Connection Error: {str(e)}", "System"

# --- RELIABLE IMAGE LINKS (Wikipedia/Wikimedia are great for this) ---
WRESTLERS = [
    {"name": "Stone Cold Steve Austin", "image": "https://upload.wikimedia.org/wikipedia/commons/e/e0/Stone_Cold_Steve_Austin.jpg"},
    {"name": "Macho Man Randy Savage", "image": "https://upload.wikimedia.org/wikipedia/commons/e/eb/Macho_Man_Randy_Savage.jpg"},
    {"name": "Ric Flair", "image": "https://upload.wikimedia.org/wikipedia/commons/1/13/Ric_Flair_July_2016.jpg"},
    {"name": "Hulk Hogan", "image": "https://upload.wikimedia.org/wikipedia/commons/4/4b/Hulk_Hogan_July_2015.jpg"}
]

NCAAB_TEAMS = [
    {"name": "Duke Blue Devils", "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Duke_Blue_Devils_logo.svg/1200px-Duke_Blue_Devils_logo.svg.png"},
    {"name": "Kentucky Wildcats", "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Kentucky_Wildcats_logo.svg/1200px-Kentucky_Wildcats_logo.svg.png"},
    {"name": "UNC Tar Heels", "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/North_Carolina_Tar_Heels_logo.svg/1200px-North_Carolina_Tar_Heels_logo.svg.png"},
    {"name": "Kansas Jayhawks", "logo": "https://upload.wikimedia.org/wikipedia/en/thumb/9/9e/Kansas_Jayhawks_logo.svg/1200px-Kansas_Jayhawks_logo.svg.png"}
]

st.title("🏀 Auto-Sleeper Legend Match")

if st.button("Fetch & Match!"):
    comment_text, username = get_latest_sleeper_comment()
    
    # Randomly pick the reaction
    wrestler = random.choice(WRESTLERS)
    team = random.choice(NCAAB_TEAMS)

    st.subheader(f"Latest from {username}:")
    st.info(comment_text)
    
    col1, col2 = st.columns(2)
    with col1:
        st.header(wrestler['name'])
        # use_container_width=True ensures images fit nicely on mobile
        st.image(wrestler['image'], use_container_width=True)
    with col2:
        st.header(team['name'])
        st.image(team['logo'], use_container_width=True)
