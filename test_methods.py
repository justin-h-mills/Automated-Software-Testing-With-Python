'''
 programmer: justin mills
     email : jmills0100@yahoo.com
description: tests methods from app, where the tests determines if the actual output
             of the methods matches with the desired output            
'''

import unittest
import app

class TestClass(unittest.TestCase):
    def test_area(self):
        # tests the method Circle.area()

        # creates a circle with radius of 2
        circle = app.Circle(2)

        # message returned when error occurs
        msg = f'area is shown {circle.area()} rather than 12.57'

        # test if the area of the above circle
        self.assertEqual(circle.area(), 12.57, msg)
    
    def test_area_negative(self):
        # tests the method Circle.area()

        # creates a circle with radius of -3
        circle = app.Circle(-3)

        # message returned when error occurs
        msg = f'area is shown {circle.area()} rather than -1'

        # test if the area of the above circle
        self.assertEqual(circle.area(), -1, msg)
    
    def test_circumference(self):
        # tests the method Circle.circumference()

        # creates a circle with radius of 5
        circle = app.Circle(5)

        # message returned when error occurs
        msg = f'circumference is shown {circle.circumference()} rather than 31.42'

        # test if the area of the above circle
        self.assertEqual(circle.circumference(), 31.42, msg)

    def test_circumference_negative(self):
        # tests the method Circle.circumference()

        # creates a circle with radius of -6
        circle = app.Circle(-6)

        # message returned when error occurs
        msg = f'circumference is shown {circle.circumference()} rather than -1'

        # test if the area of the above circle
        self.assertEqual(circle.circumference(), -1, msg)



if __name__ == '__main__':
    unittest.main()

'''
resources used:
    - https://www.geeksforgeeks.org/automated-software-testing-with-python/
    - https://docs.python.org/3/library/unittest.html?highlight=unittest#module-unittest
'''