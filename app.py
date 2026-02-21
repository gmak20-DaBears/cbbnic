def get_msg():
    url = f"https://api.sleeper.app/v1/channel/{CID}/messages?limit=1"
    
    # We try different ways Sleeper accepts the token
    # Option A: Just the token
    # Option B: "Bearer " + token
    # Option C: Use a different header name
    
    headers = {
        "Authorization": f"Bearer {TOKEN}", 
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json"
    }
    
    try:
        r = requests.get(url, headers=headers)
        # If the first way fails (401), we try without 'Bearer'
        if r.status_code == 401:
            headers["Authorization"] = TOKEN
            r = requests.get(url, headers=headers)
            
        if r.status_code == 200:
            d = r.json()
            if d: return d[0]['text'], d[0].get('display_name', 'User')
            
        return None, None
    except:
        return None, None
