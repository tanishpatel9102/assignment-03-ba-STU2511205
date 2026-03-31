# Task 1.1 Write

with open("python_notes.txt", "w", encoding="utf-8") as file:
    file.write("Topic 1: Variables store data. Python is dynamically typed.\n")
    file.write("Topic 2: Lists are ordered and mutable.\n")
    file.write("Topic 3: Dictionaries store key-value pairs.\n")
    file.write("Topic 4: Loops automate repetitive tasks.\n")
    file.write("Topic 5: Exception handling prevents crashes.\n")
print("File written successfully.")

with open("python_notes.txt", "a", encoding="utf-8") as file:
    file.write("Topic 6: Functions help organize reusable code.\n")
    file.write("Topic 7: File handling allows data persistence.\n")

print("Lines appended.")

# Task 1.2 Read

with open("python_notes.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

for i, line in enumerate(lines, start=1):
    print(f"{i}. {line.strip()}")

print("Total number of lines:", len(lines))

keyword = input("Enter a keyword to search: ").lower()
found = False

for line in lines:
    if keyword in line.lower():
        print(line.strip())
        found = True

if not found:
    print("No matching lines found.")

# Task 2.1 Fetch and Display Products:

import requests

BASE_URL = "https://dummyjson.com/products"

response = requests.get(f"{BASE_URL}?limit=20")
data = response.json()
products = data["products"]

print("ID  | Title                          | Category      | Price    | Rating")
print("----|--------------------------------|---------------|----------|-------")

for p in products:
    print(f"{p['id']:<3} | {p['title'][:30]:<30} | {p['category']:<13} | ${p['price']:<8} | {p['rating']}")

# Task 2.2 Filter and Sort

filtered = [p for p in products if p["rating"] >= 4.5]
sorted_products = sorted(filtered, key=lambda x: x["price"], reverse=True)

print("Filtered & Sorted (rating ≥ 4.5):")
for p in sorted_products:
    print(f"{p['title']} - ${p['price']} - Rating: {p['rating']}")

# Task 2.3 Search by Category

response = requests.get(f"{BASE_URL}/category/laptops")
laptops = response.json()["products"]

print("Laptops:")
for p in laptops:
    print(f"{p['title']} - ${p['price']}")

# Task 2.4 POST Request (Simulated)

new_product = {
    "title": "My Custom Product",
    "price": 999,
    "category": "electronics",
    "description": "A product I created via API"
}

response = requests.post(f"{BASE_URL}/add", json=new_product)
print("\nPOST Response:")
print(response.json())

# Task 3.1 Guarded Calculator

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Invalid input types"

print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide("ten", 2))

# Task 3.2 Guarded File Reader

def read_file_safe(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    finally:
        print("File operation attempt complete.")

print(read_file_safe("python_notes.txt"))
print(read_file_safe("ghost_file.txt"))

# Task 3.3 Robust API Calls

def safe_get(url):
    try:
        return requests.get(url, timeout=5)
    except requests.exceptions.ConnectionError:
        print("Connection failed. Please check your internet.")
    except requests.exceptions.Timeout:
        print("Request timed out. Try again later.")
    except Exception as e:
        print(e)

def safe_post(url, data):
    try:
        return requests.post(url, json=data, timeout=5)
    except requests.exceptions.ConnectionError:
        print("Connection failed. Please check your internet.")
    except requests.exceptions.Timeout:
        print("Request timed out. Try again later.")
    except Exception as e:
        print(e)

# Task 3.4 Input Validation Loop

while True:
    user_input = input("Enter a product ID to look up (1–100), or 'quit' to exit: ")

    if user_input.lower() == "quit":
        break

    if not user_input.isdigit():
        print("Invalid input. Please enter a number between 1 and 100.")
        continue

    product_id = int(user_input)

    if product_id < 1 or product_id > 100:
        print("Invalid input. Please enter a number between 1 and 100.")
        continue

    response = safe_get(f"https://dummyjson.com/products/{product_id}")

    if response:
        if response.status_code == 404:
            print("Product not found.")
        elif response.status_code == 200:
            product = response.json()
            print(f"{product['title']} - ${product['price']}")

# Task 4.1 

from datetime import datetime

def log_error(function_name, error_type, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("error_log.txt", "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] ERROR in {function_name}: {error_type} — {message}\n")
        
try:
    requests.get("https://this-host-does-not-exist-xyz.com/api", timeout=5)
except requests.exceptions.ConnectionError as e:
    log_error("fetch_products", "ConnectionError", str(e))

response = requests.get("https://dummyjson.com/products/999", timeout=5)

if response.status_code != 200:
    log_error("lookup_product", "HTTPError", f"{response.status_code} Not Found for product ID 999")

with open("error_log.txt", "r", encoding="utf-8") as file:
    print(file.read())