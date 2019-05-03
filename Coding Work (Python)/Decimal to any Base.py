binary=''
number=input("Enter a number to convert it to binary")
number=int(number)
base=input("Enter the base that you want to convert you number through")
base=int(base)

while(number>0):
    if(number % base==0):
        binary = binary + '0'
    else:
        binary = binary + '1'
    number=number//base

binary = binary[::-1]
print(binary)

decimal=int(binary, base)
print(decimal)