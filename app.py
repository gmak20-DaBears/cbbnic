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
            if d: return d[0]['text'], d[0].get('display_name', 'User'), 200
        return None, None, r.status_code
    except: return None, None, "Error"

# --- EXPANDED DATA ---
W = [
    {"n": "Stone Cold", "i": "https://i.ibb.co/XfXkMDR/stone-cold.jpg"},
    {"n": "Ric Flair", "i": "https://i.ibb.co/0Ym7K7z/ric-flair.jpg"},
    {"n": "Hulk Hogan", "i": "https://i.ibb.co/hR4y5Nn/hulk-hogan.jpg"},
    {"n": "Macho Man", "i": "https://upload.wikimedia.org/wikipedia/commons/8/87/Randy_Savage_1993.jpg"},
    {"n": "The Undertaker", "i": "https://upload.wikimedia.org/wikipedia/commons/e/e0/The_Undertaker_in_2018.jpg"},
    {"n": "Andre the Giant", "i": "https://upload.wikimedia.org/wikipedia/commons/7/77/Andre_the_Giant_1970.jpg"}
]

# Using ESPN IDs for all major colleges
T = [
    {"n": "Duke", "l": "https://a.espncdn.com/i/teamlogos/ncaa/500/150.png"},
    {"n": "Kentucky", "l": "https://a.espncdn.com/i/teamlogos/ncaa/500/96.png"},
    {"n": "Kansas", "l": "https://a.espncdn.com/i/teamlogos/ncaa/500/2305.png"},
    {"n": "North Carolina", "l": "https://a.espncdn.com/i/teamlogos/ncaa/500/153.png"},
    {"n": "UCLA", "l": "https://a.espncdn.com/i/teamlogos/ncaa/500/26.png"},
    {"n": "Indiana", "l": "https://a.espncdn.com/i/teamlogos/ncaa/500/84.png"},
    {"n": "Michigan State", "l": "https://a.espncdn.com/i/teamlogos/ncaa/500/127.png"},
    {"n": "Villanova", "l": "https://a.espncdn.com/i/teamlogos/ncaa/500/222.png"},
    {"n": "UConn", "l": "https://a.espncdn
