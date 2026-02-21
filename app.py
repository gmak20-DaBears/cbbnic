import streamlit as st
import random
import requests

# --- CONFIG ---
CHANNEL_ID = "1163193122244505600"
USER_TOKEN = "YOUR_ACTUAL_TOKEN_HERE" 

def get_comment():
    url = f"https://sleeper.com/api/v1/channel/{CHANNEL_ID}/messages?limit=1"
    headers = {"Authorization": USER_TOKEN, "User-Agent": "Mozilla/5.0"}
    try:
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            data = r.json()
            if data:
                return data[0]['text'], data[0].get('display_name', 'User')
        return f"Error {r.status_code}", "System"
    except:
        return "Connection Error", "System"

# --- DATA ---
WRESTLERS = [
    {"n": "Stone Cold", "i": "https://tinyurl.com/stonecold-pic"},
    {"n": "Ric Flair", "i": "https://tinyurl.com/ricflair-pic"},
    {"n": "Hulk Hogan", "i": "https://tinyurl.com/hogan-pic"}
]

TEAMS = [
    {"n": "Duke", "l": "https://tinyurl.com/duke-logo-pic"},
    {"n": "Kentucky", "l": "https://tinyurl.com/kentucky-logo-pic"},
    {"n": "Kansas", "l": "https://tinyurl.com/kansas-logo-pic"}
]

# --- UI ---
st.set_page_config(page_title="Sleeper Match", layout="wide")
st.title("🏀 Sleeper Legend Match")

if st.button("Fetch & Match!"):
    text, user = get_comment()
    w = random.choice(WRESTLERS)
    t = random.choice(TEAMS)

    st.subheader(f"Latest from {user}:")
    st.info(text)
    
    c1, c2 = st.columns(2)
    with c1:
        st.header(w['n'])
        st.image(w['i'], use_container_width=True)
    with c2:
        st.header(t['n'])
        st.image(t['l'], use_container_width=True)
