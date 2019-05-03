# Greatest Common Divisor
def gcd(x, y):
    while x != y:
        if x > y:
            x = x - y
        else:
            y = y - x
    return x


# Least Common Multiple
def lcm(x, y):
    if x > y:
        bigger = x
    else:
        bigger = y

    while (True):
        if (bigger % x == 0) and (bigger % y == 0):
            break
        bigger += 1

    return bigger


x = input("Enter first number")
y = input("Enter second number")

x = int(x)
y = int(y)

# result = gcd(x , y)
result = lcm(x, y)
print("The gcd is: ", result)
