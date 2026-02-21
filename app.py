importdef get_msg():
    url = f"https://api.sleeper.app/v1/channel/{CID}/messages?limit=1"
    # Added 'Bearer ' before the token - this is often the missing piece!
    headers = {
        "Authorization": f"Bearer {TOKEN}", 
        "User-Agent": "Mozilla/5.0"
    }
    try:
        r = requests.get(url, headers=headers)
        # ... rest of your code ...
        
