word = 'Happy'
lives = 10
blank = '*' * len(word)

while lives != 0:
    target = input('Enter a letter to guess' + '\n')

    if target in word.lower():
        i = 0
        while i < len(word):
            if target == word.lower()[i]:
                blank = blank[:i] + word[i] + blank[i+1:]
                i += 1
            else:
                i += 1
    else:
        print('Letter', target, 'is not in the word')
        lives -= 1

    print('You have ' + str(lives) + ' more guesses')
    print(blank)

    if blank == word:
        break