class Car:
    def __init__(self, regist_no, colour):
        self.regis_no = regist_no
        self.colour = colour

class Paint_studio:
    def paint(self, car, colour):
        car.colour = colour

car1 = Car("BBC-456", "red")
print("This car is " + car1.colour)

paint_studio = Paint_studio()
paint_studio.paint(car1, "blue")
print("This car is now " + car1.colour)