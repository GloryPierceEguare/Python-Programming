# Kaprekar Check
def Kap(a):
    i = 0

    while i < a:
        z = i * i
        y = str(z)

        if i == int(y[:len(y) // 2]) + int(y[len(y) // 2:]):
            print(i)

        i += 1

a = input("Enter the range of Kaprekar Numbers")
a = int(a)

Kap(a)
