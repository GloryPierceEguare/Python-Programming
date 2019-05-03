import time


class Clock():
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return 'The time is {}:{}:{}'.format(self.hour,self.minute,self.second)


#Main
h = int(input("Enter hour: "))
while h > 24 or h <= 0:
    h = int(input("Incorrect input! Enter hours again: "))

m = int(input("Enter minute: "))
while m > 59 or m <= 0:
    m = int(input("Incorrect input! Enter minutes again: "))

s = int(input("Enter second: "))
while s > 59 or s <= 0:
    s = int(input("Incorrect input! Enter seconds again: "))

print(mytime)

print("\nSet your alarm time.")
h = int(input("Enter hour: "))
while h > 24 or h <= 0:
    h = int(input("Incorrect input! Enter hours again: "))

m = int(input("Enter minute: "))
while m > 59 or m <= 0:
    m = int(input("Incorrect input! Enter minutes again: "))

s = int(input("Enter second: "))
while s > 59 or s <= 0:
    s = int(input("Incorrect input! Enter seconds again: "))

mytime = Clock(h, m, s)
alarm = Clock(h, m, s)

print(alarm)

if mytime != alarm:
    print("RING,RING,RING")

print(time.strftime("\nCurrent time: %H:%M:%S"))

