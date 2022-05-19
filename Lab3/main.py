# Asa Hayes
# GEOG-392
# Lab 3: OOP
# Desc: Reads in included file shapes.txt, creates a list and fills it with shape 
# objects matching the description in file, calculates area per shape

from math import pi

class Shape():
    def __init__(self, name):
        self.name = name

# rect_A = length * width
class Rectangle(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w
    def getArea(self):
        return self.l * self.w
        
# circ_A = pi * (radius ^ 2)
class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def getArea(self):
        return pi * pow(self.r, 2)
        
# tri_A = 0.5 * base * height
class Triangle(Shape):
    def __init__(self, b, h):
        self.b = b
        self.h = h
    def getArea(self):
        return 0.5 * self.b * self.h
        
# Note: This works better than readlines(), as that left the newline \n attached to the last token 
lines = open('shapes.txt', 'r').read().splitlines()
#print(lines) debug
shapeList = []

# for each line in lines, split to components, check first token for shape type, create shape and put in list
# Note: Assumes integer values for shape dimensions, casting to float would expand on this
for i in lines:
    tokens = i.split(",")
    # print(tokens)     debug
    # print(tokens[0])  debug
    if tokens[0] == 'Rectangle':
        a = Rectangle(int(tokens[1]), int(tokens[2]))
        shapeList.append(a)
    elif tokens[0] == 'Circle':
        b = Circle(int(tokens[1]))
        shapeList.append(b)
    else:
        c = Triangle(int(tokens[1]), int(tokens[2]))
        shapeList.append(c)

# print areas of each shape in order
for i in shapeList:
    print(i.getArea())
