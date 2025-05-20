class Product:
    def __init(self, name, category, price, quantity):
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def update_quantity(self, quantity):
        self.quantity = quantity

    def show_information(self):
        return f"Product: {self.name}, Category: {self.category}, Price: {self.price}, Quantity: {self.quantity}"
    
    
