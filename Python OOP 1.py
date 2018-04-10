class Car:

    numberOfCars = 0 # class variable
    def __init__(self, p_speed, p_color, p_model):
        self.speed = p_speed
        self.color = p_color
        self.model = p_model
        Car.numberOfCars = Car.numberOfCars + 1
        #print(self.speed, self.color, self.color)

    def anotherFun(self,p_name):
        self.name = p_name
        print(self.name)

    def increment(self,p_speed):
        self.speed = p_speed
        print(self.speed)

    def decrement(self,p_speed):
        self.speed =self.speed - p_speed
        print(self.speed)

    @classmethod
    def setNumber(cls):
        print(cls.numberOfCars)

BMW = Car(240, 'Black' ,2017)

camry = Car(220, 'Red', 2014)

Car.setNumber()