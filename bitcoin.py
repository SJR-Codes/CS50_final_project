"""
* CS50P Problem Set 4
* Bitcoin Price Index
* by Samu Reinikainen 25.07.2022
"""

import sys
import json
import requests as r

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
try:
    coins_to_buy = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

url = "https://api.coindesk.com/v1/bpi/currentprice.json"

try:
    response = r.get(url)
except requests.RequestException:
    sys.exit("Error connecting to coindesk.com!")

o = response.json()

try:
    rate = float((o["bpi"]["USD"]["rate"].replace(",","")))
except ValueError:
    sys.exit("Error: Rate not float!")
except IndexError:
    sys.exit("Error: rate not available!")

amount = coins_to_buy * rate
amount = '{:,.4f}'.format(amount)

print(amount)
