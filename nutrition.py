"""
* CS50P Problem Set 2
* Nutrition Facts
* by Samu Reinikainen 23.07.2022
"""

def main():
    x = input("Enter fruit: ")
    y = get_fact(x)
    if y > 0:
        print("Calories:", y)

def get_fact(x):
    facts = {
        "Apple": 130,
        "Avocado": 50,
        "Banana": 110,
        "Cantaloupe": 50,
        "Grapefruit": 60,
        "Grapes": 90,
        "Honeydew Melon": 50,
        "Kiwifruit": 90,
        "Lemon": 15,
        "Lime": 20,
        "Nectarine": 60,
        "Orange": 80,
        "Peach": 60,
        "Pear": 100,
        "Pineapple": 50,
        "Plums": 70,
        "Strawberries": 50,
        "Sweet Cherries": 100,
        "Tangerine": 50,
        "Watermelon": 80
    }

    return facts.get(x.lower().title(), 0)

main()