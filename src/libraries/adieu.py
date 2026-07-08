import inflect
p = inflect.engine()

try:
    names = []
    while True:
        name = input('Name: ')
        names.append(name)
except EOFError:
    pass

print('Adieu, adieu, to', p.join(names))