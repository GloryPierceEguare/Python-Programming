# Greatest Common Divisor
def gcd(x, y):
    while x != y:
        if x > y:
            x = x - y
        else:
            y = y - x
    return x

x = input("Enter first number")
y = input("Enter second number")

x = int(x)
y = int(y)

result = gcd(x , y)

x = x / result
y = y / result

print(x,"/",y)