PRICE = 8
DISCOUNT = {
    1: 1,
    2: 0.95,
    3: 0.9,
    4: 0.8,
    5: 0.75
}

def get_price(books):
    total_price = 0
    series_num = {i: 0 for i in range(1, 6)}

    while (books):
        series = list(set(books))
        series_num[len(series)] += 1
        books = [i for i in books if not i in series or series.remove(i)]

    # (4+4) is cheaper than (3+5)
    while (series_num.get(3, 0) and series_num.get(5, 0)):
        series_num[3] -= 1
        series_num[5] -= 1
        series_num[4] += 2
    
    for length, num in series_num.items():
        total_price += PRICE * length * num * DISCOUNT[length]

    return total_price
