import random

sent=input('Enter a sentence')

list_words = sent.split()

for word in list_words:
     first = word[0]

     last = word[-1]

     middle = word[1:-1]

     letters = list(middle)
     random.shuffle(letters)
     scrambled = ''.join(letters)

     word = first + scrambled + last

     print(word)