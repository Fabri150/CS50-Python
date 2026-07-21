vowels = 'AEIOUaeiou'

def main():
    word = input('Input: ')
    print('Output:', shorten(word))

def shorten(word):
    return ''.join('' if letter in vowels else letter for letter in word)

if __name__ == "__main__":
    main()
