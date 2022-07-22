"""
* CS50P Problem Set 1
* Deep Thought
* by Samu Reinikainen 22.07.2022
"""


answer = input("What is the answer to the meaning of life etc.? ").strip()

if answer.isnumeric() and int(answer) == 42:
    print("Yes")
elif answer.lower() == "forty-two" or answer.lower() == "forty two":
    print("Yes")
else:
    print("No")
