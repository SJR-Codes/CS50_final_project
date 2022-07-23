"""
* CS50P Problem Set 2
* Coke Machine
* by Samu Reinikainen 23.07.2022
"""

coke_price = 50
accept_change = [25, 10, 5]
amount = 0

while amount < coke_price:
    change = int(input("Enter money: "))
    if change in accept_change:
        amount += change
    if coke_price - amount > 0:
        print("Amount due:", str(coke_price - amount), " ", end="")

print("Change owed:", str(amount - coke_price), " ")