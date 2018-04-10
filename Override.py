from test import Person
class Shape:

    def printShape(self):
        print('Shape')

class Rectangle(Shape):

    def printShape(self):
        print('Rectangle')

class Circle(Shape):

    def printShape(self):
        print('Circle')

objShape = Shape()
objShape.printShape()

objRec = Rectangle()
objRec.printShape()

objCir = Circle()
objCir.printShape()

objP = Person()