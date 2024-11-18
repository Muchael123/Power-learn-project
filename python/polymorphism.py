# Base class
class Vehicle:
    def move(self):
        pass  # This will be overridden in subclasses

# Subclass for Car
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Subclass for Plane
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Subclass for Boat
class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Create instances of each vehicle
car = Car()
plane = Plane()
boat = Boat()

# Call the move method for each vehicle
vehicles = [car, plane, boat]
for vehicle in vehicles:
    vehicle.move()  # This calls the move() method for each instance
