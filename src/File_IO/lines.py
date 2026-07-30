import sys

if len(sys.argv) == 2:
    if not sys.argv[1].endswith('.py'):
        sys.exit("Not a Python File")
    try:
        with open(sys.argv[1], "r") as file:
            lines_code = []
            lines = file.readlines()
            for line in lines:
                if not line.strip().startswith('#') and not line.strip() == "":
                    lines_code.append(line)
            print(len(lines_code))
    except FileNotFoundError:
        sys.exit("File does not exist")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
else:
    sys.exit("Too many command-line arguments")