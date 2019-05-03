#Author: Glory Pierce Eguare
#Date: 06/12/18
#OS: Windows

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #Additon
    def __add__(self, sec):
        return Vector((self.x + sec.x), (self.y + sec.y))


    def __add__(self, sec):
        self.x += sec.x
        self.y += sec.y
        print('Addition')
        print(self.x,self.y)

    #Subtraction
    def __sub__(self, sec):
        return Vector((self.x - sec.x), (self.y - sec.y))


    def __sub__(self, sec):
        self.x -= sec.x
        self.y -= sec.y
        print('Subbtraction')
        print(self.x,self.y)

    #Multiplication
    def __multip__(self, sec):
        return Vector((self.x * sec.x), (self.y * sec.y))

    def __multip__(self, sec):
        self.x *= sec.x
        self.y *= sec.y
        print('Multiplication')
        print(self.x, self.y)


#Main
v1 = Vector(1, 2)
v2 = Vector(2, 2)

#Uncomment to test each instance
v1 += v2
#v1 -= v2
#v1 = v2



