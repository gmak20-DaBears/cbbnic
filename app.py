import streamlit as st
import random
import requests

# --- 1. THE KEYS ---
# IMPORTANT: This token expires often. Get a fresh one from your browser Network tab.
TK = "eyJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOiI2MTE0MjIwODY2OTQ3NjA0NDgiLCJkaXNwbGF5TmFtZSI6IkNoaUJlYXJzODQiLCJhdmF0YXIiOiJlZTRhM2VmMzY4ZGJlYzc3ZmJhOTA4ZDgxNWZiZDI4NyIsInNsZWVwZXJUb2tlbiI6ImV5SmhiR2NpT2lKSVV6STFOaUlzSW5SNWNDSTZJa3BYVkNKOS5leUpoZG1GMFlYSWlPaUpsWlRSaE0yVm1Nelk0WkdKbFl6YzNabUpoT1RBNFpEZ3hOV1ppWkRJNE55SXNJbVJwYzNCc1lYbGZibUZ0WlNJNklrTm9hVUpsWVhKek9EUWlMQ0psZUhBaU9qRTNPRGt3TVRJNU9UZ3NJbWxoZENJNk1UYzFOelEzTmprNU9Dd2lhWE5mWW05MElqcG1ZV3h6WlN3aWFYTmZiV0Z6ZEdWeUlqcG1ZV3h6WlN3aWNtVmhiRjl1WVcxbElqcHVkV3hzTENKMWMyVnlYMmxrSWpvMk1URTBNakl3T0RZMk9UUTNOakEwTkRnc0luWmhiR2xrWHpKbVlTSTZJbkJvYjI1bEluMC5FOGR3eUVfMGMtUFNoaEcxaWVoUDBwaTRhNUVWU2RFUUtxVG03LUh1a0dVIiwiZW1haWwiOiJnbWFrMjBAeWFob28uY29tIiwidHlwZSI6InNlc3Npb24iLCJpYXQiOjE3NzE2ODAwODcsImV4cCI6MTgwMzIxNjA4NywiaXNzIjoic2xlZXBlci13ZWIiLCJhdWQiOiJzbGVlcGVyLXdlYiJ9.Z6VfZzIZ-NVZFynOieVAhagnNtdhvwADbaYUND7LBbg"
ID = "1163193122244505600"

def get_msg():
    url = f"https://api.sleeper.app/v1/channel/{ID}/messages?limit=1"
    
    # We use high-fidelity headers to look like a real browser
    headers = {
        "Authorization": TK,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "Referer": "https://sleeper.com/",
        "Origin": "https://sleeper.com",
        "Accept": "application/json, text/plain, */*"
    }
    
    try:
        r = requests.get(url, headers=headers, timeout=8)
        if r.status_code == 200:
            data = r.json()
            if data and len(data) > 0:
                return data[0]['text'], data[0].get('display_name', 'User'), 200
        return None, None, r.status_code
    except Exception as e:
        return None, None, str(e)

# --- 2. THE DATA ---
W = [
    {"n": "Stone Cold", "i": "https://i.ibb.co/XfXkMDR/stone-cold.jpg"},
    {"n": "Ric Flair", "i": "https://i.ibb.co/0Ym7K7z/ric-flair.jpg"},
    {"n": "Hulk Hogan", "i": "https://i.ibb.co/hR4y5Nn/hulk-hogan.jpg"}
]

T = [
    {"n": "Duke", "l": "https://a.espncdn.com/i/teamlogos/ncaa/500/150.png"},
    {"n": "Kentucky", "l": "https://a.espncdn.com/i/teamlogos/ncaa/500/96.png"},
    {"n": "Kansas", "l": "https://a.espncdn.com/i/teamlogos/ncaa/500/2305.png"}
]

# --- 3. THE UI ---
st.set_page_config(page_title="Sleeper Matcher", layout="wide")
st.title("🤼‍♂️ Sleeper Matcher")

if st.button("Fetch & Match!", use_container_width=True):
    txt, usr, code = get_msg()
    w, t = random.choice(W), random.choice(T)
    
    if txt:
        st.success(f"Message from {usr}:")
        st.info(txt)
    else:
        st.error(f"Fetch Failed (Status: {code})")
        if code == 401:
            st.write("❌ **Your Token has expired.** You must get a new one from the browser.")
        elif code == 404:
            st.write("❌ **Channel Not Found.** Check your Channel ID.")

    st.divider()
    c1, c2 = st.columns(2)
    with c1:
        st.header(w['n'])
        st.image(w['i'], use_container_width=True)
    with c2:
        st.header(t['n'])
        st.image(t['l'], use_container_width=True)
