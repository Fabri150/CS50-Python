exp = (input('Expression: '))
x, y, z = exp.split(' ')
x = int(x)
z = int(z)

if y == '+':
    print(float(round(x+z, 1)))
elif y == '-':
    print(float(round(x-z, 1)))
elif y == '*':
    print(float(round(x*z, 1)))
elif y == '/':
    print(float(round(x/z, 1)))
else:
    print('ERROR')