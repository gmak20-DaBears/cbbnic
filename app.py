import streamlit as st
import random
import requests

# --- CONFIGURATION ---
# Replace with your actual token
USER_TOKEN = "YOUR_ACTUAL_TOKEN_HERE"
CHANNEL_ID = "1163193122244505600"

def get_sleeper_data():
    # Using the official api.sleeper.app domain for better stability
    url = f"https://api.sleeper.app/v1/channel/{CHANNEL_ID}/messages?limit=1"
    headers = {"Authorization": USER_TOKEN, "User-Agent": "Mozilla/5.0"}
    try:
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            data = r.json()
            if data:
                return data[0]['text'], data[0].get('display_name', 'User')
        return None, None
    except:
        return None, None

# --- STABLE IMAGE LINKS ---
WRESTLERS = [
    {"n": "Stone Cold", "i": "https://i.imgur.com/3vK9uIu.jpg"},
    {"n": "Ric Flair", "i": "https://i.imgur.com/WfR2fM0.jpg"},
    {"n": "Hulk Hogan", "i": "https://i.imgur.com/86D3mC4.jpg"}
]

TEAMS = [
    {"n": "Duke", "l": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Duke_Blue_Devils_logo.svg/1200px-Duke_Blue_Devils_logo.svg.png"},
    {"n": "Kentucky", "l": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Kentucky_Wildcats_logo.svg/1200px-Kentucky_Wildcats_logo.svg.png"},
    {"n": "Kansas", "l": "https://upload.wikimedia.org/wikipedia/en/thumb/9/9e/Kansas_Jayhawks_logo.svg/1200px-Kansas_Jayhawks_logo.svg.png"}
]

# --- APP UI ---
st.set_page_config(page_title="Sleeper Matcher", layout="wide")
st.title("🤼‍♂️ Sleeper Legend Matcher")

# Action Button
if st.button("Fetch & Match!"):
    text, user = get_sleeper_data()
    w = random.choice(WRESTLERS)
    t = random.choice(TEAMS)

    if text:
        st.subheader(f"Latest from: {user}")
        st.info(text)
    else:
        st.warning("⚠️ Auto-fetch failed. (Private Channel Security). Showing random match below anyway!")

    # Display Images
    col1, col2 = st.columns(2)
    with col1:
        st.header(w['n'])
        st.image(w['i'], use_container_width=True)
    with col2:
        st.header(t['n'])
        st.image(t['l'], use_container_width=True)

st.divider()
st.write("If the button above fails, paste the comment here manually:")
manual_text = st.text_input("Manual Comment Entry")
if manual_text:
    st.info(f"Judging: {manual_text}")
    
