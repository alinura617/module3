#Alinura Sultanova
#07/17/2023
#the area of a circle

import math

class circle():
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


r = int(input("Enter the radius of the circle: "))
obj = circle(r)
print("Area of the circle:", round(obj.area(), 2))
print("Circumference:", round(obj.perimeter(), 2))

#Finish