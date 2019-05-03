import random

mystring = input("Enter a word")

first = mystring[0]

last = mystring[-1]

middle = mystring[1:-1]

letters = list(middle)
random.shuffle(letters)
scrambled = ''.join(letters)

word=first + scrambled + last

print(word)