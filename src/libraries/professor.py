import random

def main():
    level = get_level()
    score = 0
    for i in range(10):
        wrong = 0
        x = generate_integer(level)
        y = generate_integer(level)
        while True:
            try:
                guess = int(input(f"{x} + {y} = "))
            except ValueError:
                guess = None
            if guess == x + y:
                score += 1
                break
            else:
                wrong += 1
                print('EEE')
                if wrong < 3:
                    continue
                else:
                    print(f"{x} + {y} = {x + y}")
                    break
    print("Score:", score)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
            else:
                pass
        except ValueError:
            pass

def generate_integer(level):
            if level == 1:
                number = random.randint(0, 9)
                return number
            elif level == 2:
                number = random.randint(10, 99)
                return number
            elif level == 3:
                number = random.randint(100, 999)
                return number
            else:
                raise ValueError

if __name__ == "__main__":
    main()