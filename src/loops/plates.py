def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if (2 <= len(s) <= 6 and s[0:2].isalpha() and s.isalnum() and valid_numbers(s)):
        return True
    else:
        return False

def valid_numbers(plate):
    found_number = False
    for letter in plate:
        if letter.isdigit():
            if not found_number and letter == '0':
                return False
            found_number = True
        if found_number and letter.isalpha():
            return False
    return True

main()