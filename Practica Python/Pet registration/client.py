class Client:
    def __init__(self, name, adress, phone):
        self.name = name
        self.adress = adress
        self.phone = phone
        self.purchase_history = []

    def update_information(self, adress=None, phone=None):
        if adress:
            self.adress = adress
        if phone:
            self.phone = phone
    
    def pucharse_registration(self, purchase):
        self.purchase_history.append(purchase)

    def show_information(self):
        return f"Client: {self.name}, Adress: {self.adress}, Phone: {self.phone}"