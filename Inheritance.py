class Person:

    def __init__(self, _name, _age):
        self.name = _name
        self.age = _age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

class Student(Person):

    def __init__(self, _name, _age):
        super().__init__(_name, _age)

    def myFun(self):
        print('My Fun')


st1 = Student('Ali', 20)

print(st1.getName())
print(st1.getAge())

















# class A:
#
#     def printA(self):
#         print("Class A")
#
# class B:
#
#     def printB(self):
#         print("Class B")
#
# class Another:
#
#     def printAnother(self):
#         print("Class B")
#
# class C(A, B, Another):
#     def printC(self):
#         print("Class C")
#
# objC = C()
# objC.printC()












# class A: # Super Class
#
#     def printA(self):
#         print('Class A')
#
#     def anotherFun(self):
#         print('Another')
#
# class B(A): # Sub Class
#
#     def printB(self):
#         print('Class B')
#         super().anotherFun()
#
#
# objA = A()
# objB = B()
# objB.printB()
