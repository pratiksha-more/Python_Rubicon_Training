
#Single Inheritance Example
class Rectangle:
    def rec_area(self, length, width):
        area= length * width
        print("Area of Rectangle:", area)


class Square(Rectangle):
    def sq_area(self, side):
        area = side * side
        print("Area of Square:", area)


obj= Square()
obj.rec_area(5, 10)  # Calculate area of rectangle
obj.sq_area(4)       # Calculate area of square


#Multiple Inheritance Example
# Vehicle
# → Common features: has wheels, moves.

# Car (inherits from Vehicle)
# → Adds: has doors, uses fuel.

# ElectricCar (inherits from Car)
# → Adds: uses battery, eco-friendly.


class Vehicle:
    def has_wheels(self):
        print("Vehicle has wheels.")

    def moves(self):
        print("Vehicle moves.")

class Car(Vehicle):
    def has_doors(self):
        print("Car has doors.")

    def uses_fuel(self):
        print("Car uses fuel.")

class ElectricCar(Car):
    def uses_battery(self):
        print("Electric car uses battery.")

    def eco_friendly(self):
        print("Electric car is eco-friendly.")  

ElectricCar_obj = ElectricCar()
ElectricCar_obj.has_wheels()  # Inherited from Vehicle  
ElectricCar_obj.moves()       # Inherited from Vehicle
ElectricCar_obj.has_doors()   # Inherited from Car  
ElectricCar_obj.uses_fuel()  # Inherited from Car
ElectricCar_obj.uses_battery()  # Specific to ElectricCar   
ElectricCar_obj.eco_friendly()  # Specific to ElectricCar
