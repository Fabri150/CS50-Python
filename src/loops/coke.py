coins = [5, 10, 25]
amount = 50

while amount > 0:
    print('Amount Due:', amount)
    coin = int(input('Insert Coin: '))
    if coin in coins:
        amount = amount - coin
else:
    print('Change Owed:', -amount)