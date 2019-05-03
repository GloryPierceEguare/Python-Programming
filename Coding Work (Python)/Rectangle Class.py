class Rectangle():
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def calc_area(self):
        return self.length * self.width

    def __str__(self):
        return '{} and {} are the length and width of the rectangle'.format(self.length, self.width)

#Main
r1 = Rectangle(3,4)

print(r1.length)
print(r1.width)

print(r1)
print(r1.calc_area())