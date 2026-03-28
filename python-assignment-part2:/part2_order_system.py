menu = [{
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}]

inventory = {
    "Paneer Tikka":   {"stock": 10, "reorder_level": 3},
    "Chicken Wings":  {"stock":  8, "reorder_level": 2},
    "Veg Soup":       {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka":      {"stock": 20, "reorder_level": 5},
    "Veg Biryani":    {"stock":  6, "reorder_level": 3},
    "Garlic Naan":    {"stock": 30, "reorder_level": 10},
    "Gulab Jamun":    {"stock":  5, "reorder_level": 2},
    "Rasgulla":       {"stock":  4, "reorder_level": 3},
    "Ice Cream":      {"stock":  7, "reorder_level": 4},
}

sales_log = {
    "2025-01-01": [
        {"order_id": 1,  "items": ["Paneer Tikka", "Garlic Naan"],          "total": 220.0},
        {"order_id": 2,  "items": ["Gulab Jamun", "Veg Soup"],              "total": 210.0},
        {"order_id": 3,  "items": ["Butter Chicken", "Garlic Naan"],        "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4,  "items": ["Dal Tadka", "Garlic Naan"],             "total": 220.0},
        {"order_id": 5,  "items": ["Veg Biryani", "Gulab Jamun"],           "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6,  "items": ["Paneer Tikka", "Rasgulla"],             "total": 260.0},
        {"order_id": 7,  "items": ["Butter Chicken", "Veg Biryani"],        "total": 570.0},
        {"order_id": 8,  "items": ["Garlic Naan", "Gulab Jamun"],           "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9,  "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"],          "total": 270.0},
    ],
}

# Task 1.1

menu_dict = menu[0]
grouped = {}

for name, details in menu_dict.items():
    category = details["category"]
    
    if category not in grouped:
        grouped[category] = []
    
    grouped[category].append((name, details))

for category, items in grouped.items():
    print(f"===== {category} =====")
    
    for name, details in items:
        status = "Available" if details["available"] else "Unavailable"
        print(f"{name:<20} ₹{details['price']:.2f}   [{status}]")
    
    print()

# Task 1.2

total_items = len(menu_dict)
print("Total items: ", total_items)

available_items = sum(1 for item in menu_dict.values() if item["available"])
print("Available items: ", available_items)

expensive_name, expensive_item = max(menu_dict.items(), key=lambda x: x[1]["price"])
print(f"Most expensive item: {expensive_name} ₹{expensive_item['price']:.2f}")

print("Item under ₹150: ")
for name, details in menu_dict.items():
    if details["price"] < 150:
        print(f"{name:<20} ₹{details['price']:.2f}")

# Task 2.1

cart = []

    if item_name not in menu_dict:
        print(f"{item_name} not found in menu.")
        return
    item = menu_dict[item_name]

    if not item ["available"]:
        print(f"{item_name} is currently unavailable.")
        return
    for cart_item in cart:
        if cart_item["item"] == item_name:
            cart_item["quantity"] += quantity
            print(f"Updated {item_name} quantity to {cart_item['quantity']}")
            return
        
    cart.append({
        "item": item_name,
        "quantity": quantity,
        "price": item["price"]
    })
    print(f"Added {item_name} x{quantity} to cart")

# Task 2.2

    def remove_from_cart(item_name):
        for cart_item in cart:
            if cart_item["item"] == item_name:
                cart.remove(cart_item)
                print(f"{item_name} removed from cart")
                return
        print(f"{item_name} not found in cart")

# Task 2.3

def update_quantity(item_name, new_quantity):
    for cart_item in cart:
        if cart_item["item"] == item_name:
            cart_item["quantity"] = new_quantity
            print(f"{item_name} quantity updated to {new_quantity}")
            return
        
    print(f"{item_name} not found in cart")

    # Task 2.4

def add_to_cart(item_name, quantity):
    if item_name not in menu_dict:
        print(f"{item_name} not found in menu.")
        return

    item = menu_dict[item_name]

    if not item["available"]:
        print(f"{item_name} is currently unavailable.")
        return

    for cart_item in cart:
        if cart_item["item"] == item_name:
            cart_item["quantity"] += quantity
            print(f"Updated {item_name} quantity to {cart_item['quantity']}")
            return

    cart.append({
        "item": item_name,
        "quantity": quantity,
        "price": item["price"]
    })
    print(f"Added {item_name} x{quantity}")


def remove_from_cart(item_name):
    for cart_item in cart:
        if cart_item["item"] == item_name:
            cart.remove(cart_item)
            print(f"{item_name} removed from cart")
            return
    print(f"{item_name} not found in cart")


def print_cart():
    print("\nCart State:")
    if not cart:
        print("Cart is empty")
        return
    
    for item in cart:
        print(f"{item['item']:<20} x{item['quantity']}  ₹{item['price']:.2f}")


add_to_cart("Paneer Tikka", 2)
print_cart()

add_to_cart("Gulab Jamun", 1)
print_cart()

add_to_cart("Paneer Tikka", 1)   
print_cart()

add_to_cart("Mystery Burger", 1)  
print_cart()

add_to_cart("Chicken Wings", 1)   
print_cart()

remove_from_cart("Gulab Jamun")
print_cart()

# Task 2.5


print("====== Order Summary ======")

subtotal = 0

for item in cart:
    item_total = item["quantity"] * item["price"]
    subtotal += item_total
    print(f"{item['item']:<18} x{item['quantity']}    ₹{item_total:.2f}")

print("------------------------------------")

gst = subtotal * 0.05
total = subtotal + gst

print(f"Subtotal:                ₹{subtotal:.2f}")
print(f"GST (5%):               ₹{gst:.2f}")
print(f"Total Payable:          ₹{total:.2f}")

print("====================================")

# Task 3.1

# Deep Copy Inventory

import copy 
inventory_backup = copy.deepcopy(inventory)

# Proving Deep copy

inventory["Gulab Jamun"]["stock"] -= 2

print("Inventory:", inventory["Gulab Jamun"])
print("Backup:", inventory_backup["Gulab Jamun"])

# Restore inventory

inventory = copy.deepcopy(inventory_backup)

# Order fulfilment

for item in cart:
    name = item["item"]
    qty = item["quantity"]

    if name in inventory:
        available = inventory[name]["stock"]

        if available >= qty:
            inventory[name]["stock"] -= qty
        else:
            print(f"⚠ Only {available} {name} available")
            inventory[name]["stock"] = 0

# Reorder alerts 

for name, details in inventory.items():
    if details["stock"] <= details["reorder_level"]:
        print(f"⚠ Reorder Alert: {name} — Only {details['stock']} unit(s) left (reorder level: {details['reorder_level']})")

# Print

print("Inventory:", inventory)
print("Backup:", inventory_backup)

# Task 4.1

print("Revenue per day: ")
revenue_per_day = {}

for date, orders in sales_log.items():
    total = sum(order["total"] for order in orders)
    revenue_per_day[date] = total
    print(f"{date}: ₹{total:.2f}")

# Task 4.2

best_day = max (revenue_per_day, key=revenue_per_day.get)
print(f"Best-selling day: {best_day} (₹{revenue_per_day[best_day]:.2f})")

# Task 4.3

item_count= {}

for orders in sales_log.values():
    for order in orders:
        unique_items = set(order["items"])
        for item in unique_items:
            item_count[item] = item_count.get(item, 0) + 1


most_ordered = max(item_count, key=item_count.get)
print(f"Most ordered item: {most_ordered} ({item_count[most_ordered]} orders)")

# Task 4.4

sales_log["2025-01-05"] = [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"], "total": 260.0},
]

# Recalculate revenue per day
print("Updated Revenue per day: ")
revenue_per_day = {}

for date, orders in sales_log.items():
    total = sum(order["total"] for order in orders)
    revenue_per_day[date] = total
    print(f"{date}: ₹{total:.2f}")

# Updated best-selling day
best_day = max(revenue_per_day, key=revenue_per_day.get)
print(f"Updated Best-selling day: {best_day} (₹{revenue_per_day[best_day]:.2f})")

# Task 4.5

print("All Orders: ")

all_orders = []
for date, orders in sales_log.items():
    for order in orders:
        all_orders.append((date, order))

for i, (date, order) in enumerate(all_orders, start=1):
    items_str = ", ".join(order["items"])
    print(f"{i}.  [{date}] Order #{order['order_id']}  — ₹{order['total']:.2f} — Items: {items_str}")
 
