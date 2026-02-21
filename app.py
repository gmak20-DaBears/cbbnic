import streamlit as st
import random

# --- DATA ---
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

st.set_page_config(page_title="Sleeper Legend Match", layout="wide")
st.title("🏀 Sleeper Legend Matcher")

# User Input
st.write("Since the Sleeper API is private, paste the comment you want to judge below!")
user_comment = st.text_input("Paste Sleeper Comment:")

if st.button("Generate Match"):
    if user_comment:
        w = random.choice(WRESTLERS)
        t = random.choice(TEAMS)

        st.success(f"Matching comment: '{user_comment}'")
        
        col1, col2 = st.columns(2)
        with col1:
            st.header(f"Legend: {w['n']}")
            st.image(w['i'], use_container_width=True)
        with col2:
            st.header(f"Team: {t['n']}")
            st.image(t['l'], use_container_width=True)
    else:
        st.warning("Please enter a comment first!")
        
