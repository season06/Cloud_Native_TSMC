PRICE = 8
DISCOUNT = {
    2: 0.95,
    3: 0.9,
    4: 0.8,
    5: 0.75
}

def get_price(books):
    return PRICE * len(books) * DISCOUNT.get(len(set(books)), 1)
