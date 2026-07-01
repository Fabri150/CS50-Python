def convert(emoji):
    emoji = emoji.replace(':)', '🙂')
    emoji = emoji.replace(':(', "🙁")
    return emoji

def main():
    emoji = input()
    print(convert(emoji))

main()