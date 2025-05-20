class Inventory:
    def __init__(self):
        self.list_products = []

    def add_product(self, product):
        self.list_products.append(product)

    def update_inventory(self, product, quantity):
        for prod in self.list_products:
            if prod.name == product.name:
                prod.update_quantity(quantity)

    def generate_warning(self, min_umbral):
        warnings = [prod.name for prod in self.list_products if prod.quantity < min_umbral]
        return f"Products under the umbral: {', '. join(warnings)}" if warnings else "There is not product under the minimum umbral"
    
