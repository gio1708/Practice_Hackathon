def add_expense(expenses, name, amount, category):
    expenses.append({"name": name, "amount": amount, "category": category})
    return expenses

def total_by_category(expenses):
    totals = {}
    for e in expenses:
        totals[e["category"]] = totals.get(e["category"], 0) + e["amount"]
    return totals
    