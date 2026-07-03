try:
    grocery = {}
    while True:
        item = input()
        item = item.upper()
        if item in grocery:
            grocery.update({item: 1 + grocery[item]})
        else:
            grocery.update({item: 1})
except EOFError:
    pass

for item in sorted(grocery):
    print(grocery[item], item)