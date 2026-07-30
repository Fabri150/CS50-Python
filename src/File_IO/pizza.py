import csv
import sys
from tabulate import tabulate

if len(sys.argv) == 2:
    if not sys.argv[1].endswith('.csv'):
        sys.exit("Not a CSV File")
    try:
        with open(sys.argv[1], "r") as file:
            prices = csv.reader(file)
            rows = list(prices)
            headers = rows[0]
            data = rows[1:]
            print(tabulate(data, headers, tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
else:
    sys.exit("Too many command-line arguments")