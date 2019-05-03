print('Enter a string to check if its a palindrome: ')
mystring = input()

upstring=mystring.upper()

#print(upstring)

revstring = upstring[::-1]

if (revstring == upstring):
    print("Palindrome")
else:
    print("Not a Palindrome")

"""for i in range(len(upstring) // 2):
    if upstring[i] != upstring[- 1 - i]:
        print('Not Palindrome')
        break
else:
    print('Palindrome')"""