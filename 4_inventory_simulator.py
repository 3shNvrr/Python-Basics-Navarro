# Inventory System Simulator

inventory = [
    {'name': 'iPhone 14 Pro', 'quantity': 15, 'price': 999.99},
    {'name': 'MacBook Pro 16"', 'quantity': 10, 'price': 2499.99},
    {'name': 'PlayStation 5', 'quantity': 8, 'price': 499.99},
    {'name': 'Samsung Galaxy S23', 'quantity': 20, 'price': 899.99},
    {'name': 'Apple Watch Series 8', 'quantity': 25, 'price': 399.99},
    {'name': 'Sony WH-1000XM5', 'quantity': 30, 'price': 349.99},
    {'name': 'Dell XPS 13', 'quantity': 12, 'price': 1199.99},
    {'name': 'GoPro HERO11', 'quantity': 18, 'price': 449.99},
    {'name': 'Amazon Echo Dot', 'quantity': 40, 'price': 49.99},
    {'name': 'Nintendo Switch OLED', 'quantity': 15, 'price': 349.99}
]

def add_product(name, quantity, price):
    for product in inventory:
        if product['name'] == name:
            print(f"Product '{name}' already exists. Use restock to add quantity.")
            return
    inventory.append({'name': name, 'quantity': quantity, 'price': price})
    print(f"Added product '{name}' with quantity {quantity} and price {price}.")

def restock_product(name, quantity):
    for product in inventory:
        if product['name'] == name:
            product['quantity'] += quantity
            print(f"Restocked '{name}'. New quantity: {product['quantity']}")
            return
    print(f"Product '{name}' not found in inventory.")

def purchase_product(name, quantity):
    for product in inventory:
        if product['name'] == name:
            if product['quantity'] >= quantity:
                product['quantity'] -= quantity
                total_price = quantity * product['price']
                print(f"Purchased {quantity} of '{name}' for ${total_price:.2f}. Remaining quantity: {product['quantity']}")
            else:
                print(f"Insufficient quantity for '{name}'. Only {product['quantity']} left.")
            return
    print(f"Product '{name}' not found in inventory.")

def total_inventory_value():
    total = 0
    for product in inventory:
        total += product['quantity'] * product['price']
    return total

def print_inventory():
    print("\nCurrent Inventory:")
    if not inventory:
        print("Inventory is empty.")
        return
    print(f"{'Name':<25}{'Quantity':<10}{'Price':<10}")
    for product in inventory:
        print(f"{product['name']:<25}{product['quantity']:<10}{product['price']:<10.2f}")
    print(f"Total inventory value: ${total_inventory_value():.2f}\n")


# Simulate some sales and restocks to show activity:
purchase_product('iPhone 14 Pro', 5)
purchase_product('PlayStation 5', 3)
restock_product('PlayStation 5', 10)
purchase_product('Amazon Echo Dot', 15)
restock_product('Amazon Echo Dot', 20)
purchase_product('MacBook Pro 16"', 2)
purchase_product('GoPro HERO11', 10)

print_inventory()
