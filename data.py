import json, os

FILE = "expenses.json"

def load_expenses():
    if not os.path.exists(FILE):
        return []
    with open(FILE) as f:
        return json.load(f)

def save_expenses(expenses):
    with open(FILE, "w") as f:
        json.dump(expenses, f)
        