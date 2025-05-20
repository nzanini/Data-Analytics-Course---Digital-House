from datetime import datetime

class Sale:
    def __init__(self, client, list_products):
        self.client = client
        self.list_products = list_products
        self.date = datetime.now()
        self.total = self.calculate_total()

    def calculate_total(self):
        return sum(product.price for product in self.list_products)
    
    def register_sale(self):
        self.client.register_sale(self)
        return f"Sale registered: {self.show_information()}"
    
    def show_information(self):
        products = ", ".join({product.name for product in self.list_products})
        return f"Client: {self.client.name}, Products: {products}, Total: {self.total}"