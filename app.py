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
            data = r.json()
            if data: return data[0]['text'], data[0].get('display_name', 'User')
    except: pass
    return None, None

# --- DATA (Swapped to new public image servers) ---
W = [
    {"n": "Stone Cold", "i": "https://www.wwe.com/f/styles/wwe_large/public/all/2019/07/Stone_Cold_Steve_Austin_stat--157451478170c9443685324523c95965.jpg"},
    {"n": "Ric Flair", "i": "https://prowrestlingpost.com/wp-content/uploads/2021/08/Ric-Flair-3.jpg"},
    {"n": "Hulk Hogan", "i": "https://www.wwe.com/f/styles/gallery_img_l/public/all/2019/10/011_CrownJewel_10312019_Logos--e4b17208159670f80877991b1f868774.jpg"}
]

T = [
    {"n": "Duke", "l": "https://identity.duke.edu/wp-content/uploads/2021/06/Logo_D-300x300.png"},
    {"n": "Kentucky", "l": "https://brandcenter.uky
