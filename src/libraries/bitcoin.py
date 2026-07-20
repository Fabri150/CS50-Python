import requests
import sys

try:
    if len(sys.argv) == 1:
       sys.exit("Missing command-line argument")
    else:
        number = sys.argv[1]
        number = float(number)
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=YourApiKey")
    content = response.json()
    price = content["data"]["priceUsd"]
    price = float(price)
except requests.RequestException:
    sys.exit("Couldn't complete request")

cost = price * number
print(f"${cost:,.4f}")