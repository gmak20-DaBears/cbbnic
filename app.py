import streamlit as st
import random
import requests

# --- CONFIGURATION ---
CHANNEL_ID = "1163193122244505600"
# Ensure you paste your TOKEN inside the quotes below
USER_TOKEN = "YOUR_ACTUAL_TOKEN_HERE" 

def get_latest_sleeper_comment():
    url = f"https://sleeper.com/api/v1/channel/{CHANNEL_ID}/messages?limit=1"
    headers = {
        "Authorization": USER_TOKEN,
        "User-Agent": "Mozilla/5.0"
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            msg_data = response.json()
            if msg_data:
                return msg_data[0]['text'], msg_data[0].get('display_name', 'User')
            return "No messages found.", "System"
        return f"Error {response.status_code}", "System"
    except:
        return "Connection Error", "System"

# --- DATA ---
WRESTLERS = [
    {"name": "Stone Cold Steve Austin", "image": "https://www.wwe.com/f/all/2018/03/001_Austin_03201997_0001--292d348a7b45494d93a778e358b53d6c.jpg"},
    {"name": "Ric Flair", "image": "
