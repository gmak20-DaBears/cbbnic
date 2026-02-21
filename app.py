import streamlit as st
import random

# 1. Data for Wrestlers
WRESTLERS = [
    {"name": "Stone Cold Steve Austin", "image": "https://upload.wikimedia.org/wikipedia/commons/e/e0/Stone_Cold_Steve_Austin.jpg"},
    {"name": "Macho Man Randy Savage", "image": "https://www.wwe.com/f/all/2016/06/Randy_Savage_pro--e8f3a388909890f5555.jpg"},
    {"name": "Ric Flair", "image": "https://www.wwe.com/f/all/2017/02/Ric_Flair_pro--f6e2e388909890f5555.jpg"},
    {"name": "The Rock", "image": "https://upload.wikimedia.org/wikipedia/commons/1/11/Dwayne_Johnson_2014_%28cropped%29.jpg"}
]

# 2. Data for NCAAB Teams (Example list)
NCAAB_TEAMS = [
    {"name": "Duke Blue Devils", "logo": "https://upload.wikimedia.org/wikipedia/commons/0/04/Duke_Blue_Devils_logo.svg"},
    {"name": "UNC Tar Heels", "logo": "https://upload.wikimedia.org/wikipedia/commons/d/d7/North_Carolina_Tar_Heels_logo.svg"},
    {"name": "Kansas Jayhawks", "logo": "https://upload.wikimedia.org/wikipedia/en/9/9e/Kansas_Jayhawks_logo.svg"},
    {"name": "Kentucky Wildcats", "logo": "https://upload.wikimedia.org/wikipedia/commons/5/5d/Kentucky_Wildcats_logo.svg"}
]

st.title("🏀 Sleeper X Wrestler X NCAAB")
st.write("Paste your Sleeper comment to get your random Legend and Team match!")

user_comment = st.text_area("Sleeper Comment:", placeholder="Paste that trash talk here...")

if st.button("Generate Reaction"):
    if user_comment:
        # Pick random items
        wrestler = random.choice(WRESTLERS)
        team = random.choice(NCAAB_TEAMS)

        st.divider()
        
        # Display Results in Columns
        col1, col2 = st.columns(2)
        
        with col1:
            st.header(f"Legend: {wrestler['name']}")
            st.image(wrestler['image'], use_container_width=True)
            
        with col2:
            st.header(f"Team: {team['name']}")
            st.image(team['logo'], use_container_width=True)

        st.success(f"**The Verdict:** Your comment has the spirit of {wrestler['name']} and the energy of {team['name']}!")
    else:
        st.warning("Enter a comment first!")
