entrees = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

try:
    sum_orders = 0
    while True:
        order = input('Item: ')
        order = order.title().strip()
        if order not in entrees:
            continue
        else:
            sum_orders += entrees[order]
            print('Total:', f'${sum_orders:.2f}')
except EOFError:
    pass