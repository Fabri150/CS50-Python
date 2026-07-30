import sys
import csv

if len(sys.argv) == 3:
    if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("Insert two csv's")
    try:
        with open(sys.argv[1], "r") as file:
            content = csv.DictReader(file)
            with open(sys.argv[2], 'w', newline='') as f:
                new_file = csv.DictWriter(f, fieldnames=("first", "last", "house"))
                new_file.writeheader()
                for row in content:
                    last, first = row["name"].rsplit(",")
                    new_file.writerow({"first": first.strip(), "last": last, "house": row["house"]})
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
else:
    sys.exit("Too many command-line arguments")