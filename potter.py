class Potter(object):

    PRICE = 8
    DISCOUNT = {
        1: 1,
        2: 0.95,
        3: 0.9,
        4: 0.8,
        5: 0.75
    }

    def __init__(self, books):
        self.books = books
        self.total_price = 0
        self.series_num = {i: 0 for i in range(1, 6)}

    def __call__(self):
        if len(self.books) == len(set(self.books)):
            return self.PRICE * len(self.books) * self.DISCOUNT.get(len(self.books), 1)

        self.arrange_books()
        self.check_cheaper()
        self.calculate_price()

        return self.total_price
        
    def arrange_books(self):
        while (self.books):
            series = list(set(self.books))
            self.series_num[len(series)] += 1
            self.books = [i for i in self.books if not i in series or series.remove(i)]

    def check_cheaper(self): # (4+4) is cheaper than (3+5)
        while (self.series_num.get(3, 0) and self.series_num.get(5, 0)):
            self.series_num[3] -= 1
            self.series_num[5] -= 1
            self.series_num[4] += 2

    def calculate_price(self):
        for length, num in self.series_num.items():
            self.total_price += self.PRICE * length * num * self.DISCOUNT[length]

