class Vehicle:
    name = ""
    licenseNumber = ""
    serialNumber = ""
    face = ""
    def turnOnAirCouditioner(self):
        print(f"Name : {self.name}")
        print("Turn On : Air")
        print("")

class Car(Vehicle):
    name = "Car"

class PickUp(Vehicle):
    name = "PickUp"

class Van(Vehicle):
    name = "Van"

class EstatwCar(Vehicle):
    name = "EstatwCar"

car1 = Car()
car1.turnOnAirCouditioner()
pickup2 = PickUp()
pickup2.turnOnAirCouditioner()
van3 = Van()
van3.turnOnAirCouditioner()
estatwcar4 = EstatwCar()
estatwcar4.turnOnAirCouditioner()