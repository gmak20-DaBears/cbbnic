import streamlit as st
import random
import requests

# --- SETTINGS ---
TK = "eyJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOiI2MTE0MjIwODY2OTQ3NjA0NDgiLCJkaXNwbGF5TmFtZSI6IkNoaUJlYXJzODQiLCJhdmF0YXIiOiJlZTRhM2VmMzY4ZGJlYzc3ZmJhOTA4ZDgxNWZiZDI4NyIsInNsZWVwZXJUb2tlbiI6ImV5SmhiR2NpT2lKSVV6STFOaUlzSW5SNWNDSTZJa3BYVkNKOS5leUpoZG1GMFlYSWlPaUpsWlRSaE0yVm1Nelk0WkdKbFl6YzNabUpoT1RBNFpEZ3hOV1ppWkRJNE55SXNJbVJwYzNCc1lYbGZibUZ0WlNJNklrTm9hVUpsWVhKek9EUWlMQ0psZUhBaU9qRTNPRGt3TVRJNU9UZ3NJbWxoZENJNk1UYzFOelEzTmprNU9Dd2lhWE5mWW05MElqcG1ZV3h6WlN3aWFYTmZiV0Z6ZEdWeUlqcG1ZV3h6WlN3aWNtVmhiRjl1WVcxbElqcHVkV3hzTENKMWMyVnlYMmxrSWpvMk1URTBNakl3T0RZMk9UUTNOakEwTkRnc0luWmhiR2xrWHpKbVlTSTZJbkJvYjI1bEluMC5FOGR3eUVfMGMtUFNoaEcxaWVoUDBwaTRhNUVWU2RFUUtxVG03LUh1a0dVIiwiZW1haWwiOiJnbWFrMjBAeWFob28uY29tIiwidHlwZSI6InNlc3Npb24iLCJpYXQiOjE3NzE2ODAwODcsImV4cCI6MTgwMzIxNjA4NywiaXNzIjoic2xlZXBlci13ZWIiLCJhdWQiOiJzbGVlcGVyLXdlYiJ9.Z6VfZzIZ-NVZFynOieVAhagnNtdhvwADbaYUND7LBbg"
ID = "1163193122244505600"

def get_msg():
    u = f"https://api.sleeper.app/v1/channel/{ID}/messages?limit=1"
    h = {"Authorization": TK, "User-Agent": "Mozilla/5.0"}
    try:
        r = requests.get(u, headers=h, timeout=5)
        if r.status_code == 200:
            d = r.json()
            if d: return d[0]['text'], d[0].get('display_name', 'User')
    except: pass
    return None, None

# --- DATA (Ultra-short links to prevent Syntax Errors) ---
W = [
    {"n": "Stone Cold", "i": "https://tinyurl.com/39wz3pjr"},
    {"n": "Ric Flair", "i": "https://tinyurl.com/3p3m9z7w"},
    {"n": "Hulk Hogan", "i": "https://tinyurl.com/mr3v2u67"}
]

T = [
    {"n": "Duke", "l": "https://tinyurl.com/4z8p4p8k"},
    {"n": "Kentucky", "l": "https://tinyurl.com/4v2n4r6v"},
    {"n": "Kansas", "l": "https://tinyurl.com/2p867u7v"}
]

# --- UI ---
st.title("🤼‍♂️ Sleeper Legend Matcher")

if st.button("Fetch & Match!"):
    txt, usr = get_msg()
    w, t = random.choice(W), random.choice(T)
    
    if txt:
        st.subheader(f"Latest from: {usr}")
        st.info(txt)
    else:
        st.warning("Fetch failed. Token might be old.")
    
    c1, c2 = st.columns(2)
    with c1:
        st.header(w['n'])
        st.image(w['i'], use_container_width=True)
    with c2:
        st.header(t['n'])
        st.image(t['l'], use_container_width=True)
