import streamlit as st
import random
import requests

# --- SETTINGS ---
TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOiI2MTE0MjIwODY2OTQ3NjA0NDgiLCJkaXNwbGF5TmFtZSI6IkNoaUJlYXJzODQiLCJhdmF0YXIiOiJlZTRhM2VmMzY4ZGJlYzc3ZmJhOTA4ZDgxNWZiZDI4NyIsInNsZWVwZXJUb2tlbiI6ImV5SmhiR2NpT2lKSVV6STFOaUlzSW5SNWNDSTZJa3BYVkNKOS5leUpoZG1GMFlYSWlPaUpsWlRSaE0yVm1Nelk0WkdKbFl6YzNabUpoT1RBNFpEZ3hOV1ppWkRJNE55SXNJbVJwYzNCc1lYbGZibUZ0WlNJNklrTm9hVUpsWVhKek9EUWlMQ0psZUhBaU9qRTNPRGt3TVRJNU9UZ3NJbWxoZENJNk1UYzFOelEzTmprNU9Dd2lhWE5mWW05MElqcG1ZV3h6WlN3aWFYTmZiV0Z6ZEdWeUlqcG1ZV3h6WlN3aWNtVmhiRjl1WVcxbElqcHVkV3hzTENKMWMyVnlYMmxrSWpvMk1URTBNakl3T0RZMk9UUTNOakEwTkRnc0luWmhiR2xrWHpKbVlTSTZJbkJvYjI1bEluMC5FOGR3eUVfMGMtUFNoaEcxaWVoUDBwaTRhNUVWU2RFUUtxVG03LUh1a0dVIiwiZW1haWwiOiJnbWFrMjBAeWFob28uY29tIiwidHlwZSI6InNlc3Npb24iLCJpYXQiOjE3NzE2ODAwODcsImV4cCI6MTgwMzIxNjA4NywiaXNzIjoic2xlZXBlci13ZWIiLCJhdWQiOiJzbGVlcGVyLXdlYiJ9.Z6VfZzIZ-NVZFynOieVAhagnNtdhvwADbaYUND7LBbg"
CID = "1163193122244505600"

def get_msg():
    url = f"https://api.sleeper.app/v1/channel/{CID}/messages?limit=1"
    headers = {"Authorization": TOKEN, "User-Agent": "Mozilla/5.0"}
    try:
        r = requests.get(url, headers=headers, timeout=5)
        if r.status_code == 200:
            d = r.json()
            if d: return d[0]['text'], d[0].get('display_name', 'User')
    except: pass
    return None, None

# --- DATA (Using direct-access
