class ComplexNumber():
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def __add__(self):
        #new_a = self.__a + self.__b
        #new_b = self.__b + c.get_imaginery()
        return self.__a + self.__b

    def __sub__(self, c):
        new_a = self.__a + c.get_real()
        new_b = self.__b + c.get_imaginery()
        return ComplexNumber(new_a, new_b)

#print("Addition of two complex numbers : ",(4+3j)+(3-7j))

#a = (2+5i)
#b = (3+2i)

#n = CompleNumber(a, b)

numbers = ComplexNumber(2+5j, 3+2j)

print(numbers.__add__())
