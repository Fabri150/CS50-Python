def main():
    time = input('What time is it? ')
    time = convert(time)
    return time

def convert(time):
    hours, minutes = time.split(':')
    hours = float(hours)
    minutes = float(minutes)
    time = hours + (minutes / 60)
    return time

if __name__ == "__main__":
    time = main()
    if 7 <= time <= 8:
        print('breakfast time')
    elif 12 <= time <= 13:
        print('lunch time')
    elif 18 <= time <= 19:
        print('dinner time')