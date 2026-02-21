import streamlit as st
import random
import requests

# --- CONFIGURATION ---
# This is the Channel ID you provided
CHANNEL_ID = "1163193122244505600"
# Ensure your token is correct!
USER_TOKEN = "YOUR_ACTUAL_TOKEN_HERE" 

def get_latest_sleeper_comment():
    # UPDATED URL: Using the specific channel messages endpoint
    url = f"https://sleeper.com/api/v1/channel/{CHANNEL_ID}/messages?limit=1"
    
    headers = {
        "Authorization": USER_TOKEN,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            msg_data = response.json()
            if msg_data and len(msg_data) > 0:
                return msg_data[0]['text'], msg_data[0].get('display_name', 'User')
            return "No messages found.", "System"
        else:
            # This helps us see the exact error code (401, 404, etc.)
            return f"Error {response.status_code}: Connection failed.", "System"
    except Exception as e:
        return f"Error: {str(e)}", "System"

# --- FIXED IMAGE LINKS (Direct URLs) ---
WRESTLERS = [
    {"name": "Stone Cold Steve Austin", "image": "https://upload.wikimedia.org/wikipedia/commons/e/e0/Stone_Cold_Steve_Austin.jpg"},
    {"name": "Macho Man Randy Savage", "image": "https://upload.wikimedia.org/wikipedia/commons/e/eb/Macho_Man_Randy_Savage.jpg"},
    {"name": "Ric Flair", "image": "https://upload.wikimedia.org/wikipedia/commons/1/13/Ric_Flair_July_2016.jpg"}
]

NCAAB_TEAMS = [
    {"name": "Duke Blue Devils", "logo": "https://upload.wikimedia.org/wikipedia/commons/0/04/Duke_Blue_Devils_logo.svg"},
    {"name": "Kentucky Wildcats", "logo": "https://upload.wikimedia.org/wikipedia/commons/5/5d/Kentucky_Wildcats_logo.svg"},
    {"name": "Kansas Jayhawks", "logo": "https://upload.wikimedia.org/wikipedia/en/9/9e/Kansas_Jayhawks_logo.svg"}
]

st.title("🏀 Auto-Sleeper Legend Match")

if st.button("Fetch & Match!"):
    comment_text, username = get_latest_sleeper_comment()
    
    wrestler = random.choice(WRESTLERS)
    team = random.choice(NCAAB_TEAMS)

    st.subheader(f"Latest from {username}:")
    st.info(comment_text)
    
    col1, col2 = st.columns(2)
    with col1:
        st.header(wrestler['name'])
        # Use_container_width=True makes it look great on mobile phones
        st.image(wrestler['image'], use_container_width=True)
    with col
