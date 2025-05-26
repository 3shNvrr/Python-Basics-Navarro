# Inventory System Simulator

inventory = {}

def add_product(name, quantity, price):
    if name in inventory:
        print(f"{name} is already in inventory.")
    else:
        inventory[name] = {'quantity': quantity, 'price': price}
        print(f"Added {name} with quantity {quantity} and price {price}.")

def restock_product(name, quantity):
    if name in inventory:
        inventory[name]['quantity'] += quantity
        print(f"Restocked {name}. New quantity: {inventory[name]['quantity']}")
    else:
        print(f"{name} is not in inventory.")

def purchase_product(name, quantity):
    if name in inventory:
        if inventory[name]['quantity'] >= quantity:
            inventory[name]['quantity'] -= quantity
            cost = quantity * inventory[name]['price']
            print(f"Purchased {quantity} of {name}. Cost: ${cost:.2f}")
        else:
            print(f"Not enough {name} in stock. Current quantity: {inventory[name]['quantity']}")
    else:
        print(f"{name} is not in inventory.")

def total_inventory_value():
    total = 0
    for product in inventory.values():
        total += product['quantity'] * product['price']
    return total

# Example usage - adding 10 products
add_product("Laptop", 5, 800)
add_product("Smartphone", 10, 500)
add_product("Headphones", 15, 50)
add_product("Keyboard", 7, 30)
add_product("Mouse", 20, 25)
add_product("Monitor", 8, 150)
add_product("Printer", 3, 120)
add_product("Tablet", 6, 300)
add_product("USB Cable", 50, 5)
add_product("External Hard Drive", 4, 100)

# Restock more products with bigger amounts
restock_product("Laptop", 10)
restock_product("USB Cable", 40)
restock_product("Monitor", 15)

# Purchase more products
purchase_product("Smartphone", 8)
purchase_product("Monitor", 10)
purchase_product("Mouse", 15)
purchase_product("Headphones", 10)

print(f"Total inventory value: ${total_inventory_value():.2f}")
