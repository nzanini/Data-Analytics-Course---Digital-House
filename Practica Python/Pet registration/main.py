#functions for the consola interfaz

from clases.pet import Dog, Cat
from clases.client import Client
from clases.inventory import Inventory
from clases.sale import Sale
from clases.product import Product

def register_pet():
    type = input("give the pet's type (cat/dog): ").strip().lower()
    name = input("give the pet's name: ")
    age = int(input("give the pet's age: "))
    health = input("health state: ")
    price = float(input("pet's price: "))

    if type == "dog":
        race = input("dog's race: ")
        energy_level = input("Dog's energy level: ")
        pet = Dog(name, age, health, price, race, energy_level)

    elif type == "cat":
        race = input("Cat's race: ")
        independency = input("Cat's independency: ")
        pet = Cat(name, age, health, price, race, independency)

    else:
        print("type no recognized")
        return
    
    return pet

def register_client():
    name = input("Client's name: ")
    adress = input("Client's adress: ")
    phone = input("Client's phone: ")
    client = Client(name, adress, phone)
    return client

def register_product():
    name = input("Product's name: ")
    category = input("Product's category: ")
    price = float(input("Product's price: "))
    quantity = int(input("Product's quantity: "))
    product = Product(name, category, price, quantity)
    return product

def register_sale(client, inventory):
    client_name = input("Client's name: ")
    client = next((c for c in client if c.name == client_name), None)
    if not client:
        print("no client")
        return
    
    products = []

    while True:
        product_name = input("product's name(leave empty for ending): ")
        if not product_name:
            break
        product = next((p for p in inventory.list_products if p.name == product_name), None)
        if product:
            products.append(product)
        else: 
            print("no product")

        if products:
            sale = Sale(client, products)
            sale.register_sale()
            print("The sale has ben registered")
        else: 
            print("There is not products registered for the sale")

def show_menu():
    print("\n --- Menu ---")
    print("1. Register pet")
    print("2. Register client")
    print("3. Register product")
    print("4. Register sale")
    print("5. Show pet information")
    print("6. Show client information")
    print("7. Show product information")
    print("8. Generate inventory warning")
    print("9. Exit")

def main():
    pets = []
    clients = []
    inventory = Inventory()

    while True:
        show_menu()
        option = input("Select an option: ")

        if option == "1":
            pet = register_pet()
            if pet:
                pets.append(pet)
                print("Pet registered")

        elif option == "2":
            client = register_client()
            if client: 
                clients.append(client)
                print("Client registered")
        
        elif option == "3":
            product = register_product()
            if product:
                inventory.add_product(product)
                print("product registered")

        elif option == "4":
            register_sale(clients, inventory)
        elif option == "5":
            for pet in pets:
                print(pet.show_information())
                if isinstance(pet, Dog) or isinstance(pet, Cat):
                    print(pet.show_caracteristics())

        elif option == "6":
            for client in clients:
                print(client.show_information())

        elif option == "7":
            for product in inventory.list_products:
                print(product.show_information())

        elif option == "8":
            min_umbral = int(input("give the minimum umbral of the inventory: "))
            print(inventory.generate_warning(min_umbral))

        elif option == "9":
            print("Thanks for using the APP!")
            break

        else: 
            print("option no valided. Try again.")

if __name__ == "__main__":
    main()

