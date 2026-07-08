import random

def main():
    level = get_level()
    generate_integer(level)


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
    score = 0
    for i in range(10):
        if level == 1:
            x = random.randint(0, 10)
            y = random.randint(0, 10)
            guess = int(input(f"{x} + {y} = "))
            if guess == x + y:
                score += 1
                continue
            else:
                print('EEE')
                continue
    print("Score: ", score)

if __name__ == "__main__":
    main()