def get_msg():
    url = f"https://api.sleeper.app/v1/channel/{ID}/messages?limit=1"
    
    # We try with 'Bearer ' prefix first, then without it
    for prefix in ["Bearer ", ""]:
        headers = {
            "Authorization": f"{prefix}{TK}", 
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Content-Type": "application/json"
        }
        try:
            r = requests.get(url, headers=headers, timeout=5)
            if r.status_code == 200:
                data = r.json()
                if data:
                    return data[0]['text'], data[0].get('display_name', 'User')
        except:
            continue
    return None, None
