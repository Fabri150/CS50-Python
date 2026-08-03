import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    if match := re.fullmatch(r"([1-9]|1[0-2])(?::([0-5][0-9]))? (AM|PM) to ([1-9]|1[0-2])(?::([0-5][0-9]))? (AM|PM)", s):
        first_hour = new_hour(match.group(1), match.group(2), match.group(3))
        second_hour = new_hour(match.group(4), match.group(5), match.group(6))
        return f"{first_hour} to {second_hour}"
    else:
        raise ValueError

def new_hour(hour, minutes, meridiem):
    hour = int(hour)
    if (1 <= hour <= 11 and meridiem == "AM") or (hour == 12 and meridiem == "PM"):
        final_hour = hour
    elif 1 <= hour <= 11 and meridiem == "PM":
            final_hour = hour + 12
    else:
            final_hour = hour - 12
    if minutes != None:
        minutes = int(minutes)
        final_minutes = minutes
        return f"{final_hour:02d}:{final_minutes:02d}"
    else:
        return f"{final_hour:02d}:00"

if __name__ == "__main__":
    main()