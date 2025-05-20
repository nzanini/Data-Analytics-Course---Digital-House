class Pets:
    def __init__(self, name, age, health, price, race):
        self.name = name
        self.age = age
        self.health = health
        self.price = price
        self.race = race

    def update_information(self, age=None, health=None, price=None, race=None):
        if age:
            self.age = age
        if health:
            self.health = health
        if price:
            self.price = price
        if race:
            self.race = race

    def show_information(self):
        return f"Pet: {self.name}, Age: {self.age}, Health: {self.health}, Price: {self.price}, Race: {self.race}"
    
class Dog(Pets):

    def __init__(self, name, age, health, price, race, energy_level):
        super().__init__(name, age, health, price, race)

        self.energy_level = energy_level

    def show_characteristics(self):
        return f"Energy level: {self.energy_level}"
    
class Cat(Pets):

    def __init__(self, name, age, health, price, race, independence):
        super().__init__(name, age, health, price, race)

        self.independence = independence

    def show_caracteristics(self):
        return f"Independence: {self.independence}"