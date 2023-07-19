class Vehicle:
    def __init__(self, name, price, color="blue", type="Crossland"): #constructor
        self.name = name
        self.type = type
        self.color = color
        self.price = price
    def description(self):
        return f"name: {self.name} color: {self.color} type: {self.type} price: {self.price}"

vehicles_list = []
for _ in range(1):
    car_name = input("enter vehicle name: ")
    car_price = input("enter vehicle price: ")
    user_decision = input("do you want car type and color")

    if user_decision == "yes":
        car_type = input("enter vehicle type: ")
        car_color = input ("enter vehicle color")
        vehicles_list.append(Vehicle(car_name, car_price, car_color, car_type))
    else:
        vehicles_list.append(Vehicle(car_name, car_price))

for detail in vehicles_list:
    print(detail.description())


# PRIVATE, MANGLED AND PUBLIC VARIABLE
# conventionally we use one underscore to prefix a private variable, but its also accessible
# Mangled variables is created with two underscore and its seen to be private, but its still accessible if we can enter the class or clock of code where the variable is created
