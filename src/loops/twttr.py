vowels = 'aeiouAEIOU'

word = input('Input: ')

print('Output:', ''.join('' if letter in vowels else letter for letter in word))