'''
 programmer: justin mills
     email : jmills0100@yahoo.com
description: creates an circle object of a given radius
'''

from math import pi

class Circle():
    def __init__(self, radius):
        # creates a circle with a given radius
        self.radius = radius
    
    def area(self):
        # returns area of the circle rounded to the tens place
        return round(pi * self.radius**2, 2)
    
    def circumference(self):
        # returns circumference of the circle rounded to the tens place
        return round(2 * pi * self.radius, 2)
    
    def __repr__(self):
        # declares how a circle object should be displayed
        return f'\ncircle dimensions\nradius: {self.radius}\narea: {self.area()}\ncircumference: {self.circumference()}\n'

if __name__ == '__main__':
    # read input from user
    radius = int(input('\nenter the radius of circle:\n\n>>> '))

    # creates circle with the provided radius
    circle = Circle(radius)

    # displays created circle to console
    print(circle)