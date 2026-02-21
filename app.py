# --- CONFIG ---
CHANNEL_ID = "1163193122244505600"
USER_TOKEN = "YOUR_ACTUAL_TOKEN_HERE" 

def get_comment():
    # THIS IS THE API URL
    url = f"https://sleeper.com/api/v1/channel/{CHANNEL_ID}/messages?limit=1"
    
