class Phone:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

phone1 = Phone("Samsung", 500)
print(phone1.price)

phone1.price = 450
print(phone1.price)
