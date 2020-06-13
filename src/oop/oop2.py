
class GroundVehicle():
    def __init__(self, num_wheels=4):
        self.num_wheels = num_wheels

    def drive(self, noise="vroooom"):
        return noise


class Motorcycle(GroundVehicle):
    def __init__(self, num_wheels=2):
        self.num_wheels = num_wheels

    def drive(self, noise="BRAAAP!!"):
        return noise


vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]


print(vehicles[0].drive())
print(vehicles[1].drive())
print(vehicles[2].drive())
print(vehicles[3].drive())
print(vehicles[4].drive())