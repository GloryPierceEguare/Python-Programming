class Address:
    def __init__(self, number, name, city):
        self.__number = number
        self.__name = name
        self.__city = city

    def display(self):
        print(self.__number, self.__name, self.__city)


class OfficeAddress:
    def __init__(self, office_no, office_name, number, name, city):
        self.__office_no = office_no
        self.__office_name = office_name
        self.__number = number
        self.__name = name
        self.__city = city

    def display(self):
        print(self.__office_no, self.__office_name, self.__number, self.__name, self.__city)


#Main
x = Address(15, 'Mist Park,', '\nDublin.\n')
x.display()

y = OfficeAddress(203, 'Boat House,', '\n40', 'Mist Park,', '\nDublin.')
y.display()