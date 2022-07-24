"""
* CS50P Problem Set 3
* Felipe’s Taqueria
* by Samu Reinikainen 24.07.2022
"""

def main():
    price = (get_input("What's your pleasure, sir? "))

    print(f"Total: ${price:.2f}")

def get_input(prompt):
    price = 0
    while True:
        try:
            price += get_price(input(prompt))
            print(f"Total: ${price:.2f}", end=" ")
        except EOFError:
            return price

def get_price(item):
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    return menu.get(item.lower().title(), 0)

main()