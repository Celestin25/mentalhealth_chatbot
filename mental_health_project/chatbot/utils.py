import json
import random
import difflib
from pathlib import Path

def load_intent_data():
    data_dir = Path(__file__).resolve().parent.parent / 'data'
    
    try:
        with open(data_dir / 'intents.json') as f:
            intents_data_en = json.load(f)
        with open(data_dir / 'kiny.json') as f:
            intents_data_rw = json.load(f)
    except FileNotFoundError:
        intents_data_en = {"intents": []}
        intents_data_rw = {"intents": []}
    
    return intents_data_en, intents_data_rw

def get_chatbot_response(message: str, language: str = 'en'):
    intents_data_en, intents_data_rw = load_intent_data()
    intents_data = intents_data_en if language == 'en' else intents_data_rw
    
    message = message.lower()
    all_patterns = [pattern.lower() 
                   for intent in intents_data['intents'] 
                   for pattern in intent['patterns']]
    
    close_matches = difflib.get_close_matches(message, all_patterns, n=1, cutoff=0.5)
    
    if close_matches:
        matched_pattern = close_matches[0]
        for intent in intents_data['intents']:
            if matched_pattern in [p.lower() for p in intent['patterns']]:
                return random.choice(intent['responses'])
    
    return ("I don't have an answer for that right now. Please consult a professional."
            if language == 'en'
            else "Ndasaba imbabazi, sinshobora kubona igisubizo kuri ibyo.")