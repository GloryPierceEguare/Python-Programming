binary=''
print('"Enter a number to convert it to binary"')
number=input("Enter a number to convert it to binary")
number=int(number)

while(number>0):
    if(number % 2==0):
        binary = binary + '0'
    else:
        binary = binary + '1'
    number=number//2

binary = binary[::-1]
print(binary)

decimal=int(binary, 2)
print(decimal)