class Car:
    make = ""
    model = ""
    def __init__(self, make, model):     # constructor
        self.make = make
        self.model = model

    def drive(self):    # user defined function
        return "this car is driving"

tolu_car = Car("Toyota", "Camry")
uche_car = Car("Opel", "Crossland")

print(tolu_car.make, tolu_car.model)
print(uche_car.make, uche_car.model, uche_car.drive())

tolu_car.make = "Mercedes" # change the value of the object
uche_car.model = "Mokka"

print(tolu_car.make, tolu_car.model)
print(uche_car.make, uche_car.model, uche_car.drive())
