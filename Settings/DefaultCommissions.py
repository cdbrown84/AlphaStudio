
def getCommissions(quantity, fill_cost):
    full_cost = 1.3
    if quantity <= 500:
        full_cost = max(1.3, 0.013 * quantity)
    else:  # Greater than 500
        full_cost = max(1.3, 0.008 * quantity)
    full_cost = min(full_cost, 0.5 / 100.0 * quantity * fill_cost)
    return full_cost