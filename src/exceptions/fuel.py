while True:
    fraction = input('Fraction: ')
    try:
        x, y = fraction.split('/')
        x = int(x)
        y = int(y)
    except (ValueError, TypeError):
        pass
    else:
        if -1 < x <= y and y > 0:
            fuel = (x / y) * 100
        else:
            continue
        if fuel <= 1:
            print('E')
            break
        elif fuel >= 99:
            print('F')
            break
        else:
            print(f'{round(fuel)}%')
            break

