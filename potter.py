PRICE = 8
DISCOUNT = {
    2: 0.95,
    3: 0.9,
    4: 0.8,
    5: 0.75
}

def get_price(books):
    if len(books) == len(set(books)) or len(set(books)) == 1:
        return PRICE * len(books) * DISCOUNT.get(len(set(books)), 1)

    total_price = 0
    while (books):
        series = list(set(books))
        total_price += PRICE * len(series) * DISCOUNT.get(len(series), 1)
        books = [i for i in books if not i in series or series.remove(i)]

    return total_price
