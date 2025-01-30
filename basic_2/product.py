class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def update_price(self, new_price):
        self.price = new_price

    def add_stock(self, quantity):
        self.stock += quantity

    def sell(self, quantity):
        if quantity > self.stock:
            raise ValueError("not enough quantity")
        else:
            self.stock -= quantity
