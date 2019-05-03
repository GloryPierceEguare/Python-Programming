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

def addFrac(t1, t2):
  den = lcm(t1[1], t2[1])
  A = den / t1[1] * t2[0]
  B = den / t1[1] * t2[0]
  num = A + B
  GCD = gcd( num, den )
  return [num / GCD, den / GCD]

def subFrac(t1, t2):
    den = lcm(t1[1], t2[1])
    A = den / t1[1] * t1[0]
    B = den / t2[1] * t2[0]
    num = A - B;
    GCD = gcd(0 > num and -num or num, den)
    GCD = 0 > GCD and -GCD or GCD
    return [num / GCD, den / GCD]


a = input("Enter the numerator of the 1st fraction")
b = input("Enter the denominator of the 1st fraction")
x = input("Enter the numerator of the 2nd fraction")
y = input("Enter the denominator of the 2nd fraction")

a = int(a)
b = int(b)
x = int(x)
y = int(y)

t1 = (a, b)
t2 = (x, y)

#result = addFrac((a, b), (x, y))
result = subFrac((a, b), (x, y))
print("The fraction is: ", result[0],"/", result[1])