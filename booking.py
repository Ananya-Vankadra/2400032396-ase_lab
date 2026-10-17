
def calculate_ticket_price(price, tickets):
    if price <= 0 or tickets <= 0:
        raise ValueError("Price and tickets must be positive")
    return price * tickets
