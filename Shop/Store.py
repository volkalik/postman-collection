class Product():

    def __init__(self, name, color, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.color = color

    def total_cost(self):
        total = self.price * self.quantity
        return total



