# db_handler.py
import json
import os
import uuid
from datetime import datetime

HISTORY_FILE = "history.json"

def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []
    with open(HISTORY_FILE, "r") as file:
        return json.load(file)

def save_history(history_data):
    with open(HISTORY_FILE, "w") as file:
        json.dump(history_data, file, indent=4)

def add_entry(headline, content, place, person, image_prompt=""):
    history = load_history()
    new_entry = {
        "id": str(uuid.uuid4()),
        "date": datetime.now().strftime("%B %d, %Y - %I:%M %p"),
        "headline": headline,
        "content": content,
        "place": place,
        "person": person,
        "image_prompt": image_prompt
    }
    history.insert(0, new_entry)
    save_history(history)
    return new_entry

def delete_entry(item_id):
    history = load_history()
    history = [item for item in history if item["id"] != item_id]
    save_history(history)

def clear_all():
    save_history([])