#86. Write a Python program to get the ASCII value of a character.
def get_ASCII(char):
    return ord(char)


character = input('Enter a character: ')
print(get_ASCII(character))