"""def sum_digits_sqr(n):
    a = n
    rem = 0
    sum = 0
    while a != 0:
        rem = a % 10
        sum += rem ** 2
        a /= 10
    return sum


n = int(input("Enter number: "))
a = n

while sum_digits_sqr(n) != 1:
    n = sum_digits_sqr(n)
    if sum_digits_sqr(n) == 1:
        print("Happy number")
    else:
        print("Not a Happy Number")
    break"""

a = int(input("Enter a number to check if it is happy: "))
l = map(int, str(a))
while 1:
    c = 0
    for i in l:
       b = i
       c = c + b **2
    if c == 1:
        print("Happy Number!")
        input("Hit enter to end")
        break
    elif c == 4:
        print ("Not a Happy number")
        input("Hit enter to end")
        break
    else:
        l = map(int, str(c))