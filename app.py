import streamlit as st
import random
import requests

# --- 1. CONFIGURATION ---
# Using your provided ChiBears84 token and Channel ID
TK = "eyJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOiI2MTE0MjIwODY2OTQ3NjA0NDgiLCJkaXNwbGF5TmFtZSI6IkNoaUJlYXJzODQiLCJhdmF0YXIiOiJlZTRhM2VmMzY4ZGJlYzc3ZmJhOTA4ZDgxNWZiZDI4NyIsInNsZWVwZXJUb2tlbiI6ImV5SmhiR2NpT2lKSVV6STFOaUlzSW5SNWNDSTZJa3BYVkNKOS5leUpoZG1GMFlYSWlPaUpsWlRSaE0yVm1Nelk0WkdKbFl6YzNabUpoT1RBNFpEZ3hOV1ppWkRJNE55SXNJbVJwYzNCc1lYbGZibUZ0WlNJNklrTm9hVUpsWVhKek9EUWlMQ0psZUhBaU9qRTNPRGt3TVRJNU9UZ3NJbWxoZENJNk1UYzFOelEzTmprNU9Dd2lhWE5mWW05MElqcG1ZV3h6WlN3aWFYTmZiV0Z6ZEdWeUlqcG1ZV3h6WlN3aWNtVmhiRjl1WVcxbElqcHVkV3hzTENKMWMyVnlYMmxrSWpvMk1URTBNakl3T0RZMk9UUTNOakEwTkRnc0luWmhiR2xrWHpKbVlTSTZJbkJvYjI1bEluMC5FOGR3eUVfMGMtUFNoaEcxaWVoUDBwaTRhNUVWU2RFUUtxVG03LUh1a0dVIiwiZW1haWwiOiJnbWFrMjBAeWFob28uY29tIiwidHlwZSI6InNlc3Npb24iLCJpYXQiOjE3NzE2ODAwODcsImV4cCI6MTgwMzIxNjA4NywiaXNzIjoic2xlZXBlci13ZWIiLCJhdWQiOiJzbGVlcGVyLXdlYiJ9.Z6VfZzIZ-NVZFynOieVAhagnNtdhvwADbaYUND7LBbg"
ID = "1163193122244505600"

def get_msg():
    url = f"https://api.sleeper.app/v1/channel/{ID}/messages?limit=1"
    # We send the Authorization header exactly how the browser does
    headers = {
        "Authorization": TK, 
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    try:
        r = requests.get(url, headers=headers, timeout=5)
        if r.status_code == 200:
            data = r.json()
            if data and len(data) > 0:
                return data[0]['text'], data[0].get('display_name', 'User')
        return None, r.status_code # Returns the error code if it fails
    except Exception as e:
        return None, str(e)

# --- 2. DATA (Wrestlers & Teams) ---
WRESTLERS = [
    {"n": "Stone Cold", "i": "https://www.wrestling-online.com/news/wp-content/uploads/2021/03/stonecold-1.jpg"},
    {"n": "Ric Flair", "i": "https://www.wrestling-online.com/news/wp-content/uploads/2017/08/ricflair.jpg"},
    {"n": "Hulk Hogan", "i": "https://www.wrestling-online.com/news/wp-content/uploads/2015/07/hulkhogan.jpg"}
]

TEAMS = [
    {"n": "Duke", "l": "https://a.espncdn.com/i/teamlogos/ncaa/500/150.png"},
    {"n": "Kentucky", "l": "https://a.espncdn.com/i/teamlogos/ncaa/500/96.png"},
    {"n": "Kansas", "l": "https://a.espncdn.com/i/teamlogos/ncaa/500/2305.png"}
]

# --- 3. UI LAYOUT ---
st.set_page_config(page_title="Sleeper Legend Matcher", layout="wide")
st.title("🤼‍♂️ Sleeper Legend Matcher")
st.markdown("---")

if st.button("Fetch Last Message & Match!", use_container_width=True):
    msg_text, status = get_msg()
    wrestler = random.choice(WRESTLERS)
    team = random.choice(TEAMS)
    
    # Message Display
    if msg_text:
        st.success(f"**Latest Message fetched successfully!**")
        st.info(f"🗨️ **{status}**: {msg_text}")
    else:
        st.error(f"⚠️ **Fetch failed.** (Status: {status})")
        st.write("This usually means the token is expired. Refresh your token in the code.")

    st.markdown("---")
    
    # Columns for Wrestler and Team
    col1, col2 = st.columns(2)
    
    with col1:
        st.header(f"🔥 {wrestler['n']}")
        st.image(wrestler['i'], use_container_width=True)
        
    with col2:
        st.header(f"🏀 {team['n']}")
        st.image(team['l'], use_container_width=True)
        
