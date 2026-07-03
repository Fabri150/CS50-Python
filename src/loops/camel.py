camel = input('camelCase: ')

print('snake_case:', ''.join('_' + word.lower() if word.isupper() else word for word in camel))