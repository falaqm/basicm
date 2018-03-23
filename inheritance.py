class Vehicle():
    def general_usage(self):
        print('General use:transportation')
class Car(Vehicle):
    def __init__(self):
        print("i am car")
        self.wheels=4
        self.roof=True
    def specific_usage(self):
        self.general_usage()
        print("Family and work")
class bike(Vehicle):
    def __init__(self):
        print("i am bike")
        self.wheels=2
        self.roof=False
    def specific_usage(self):
        self.general_usage()
        print("Trips and racing")

c=Car()
c.specific_usage()
print('*'*50)
m=bike()
m.specific_usage()
print('*'*50)
print(isinstance(c,bike))
print(issubclass(Car,bike))


