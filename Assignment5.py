# Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
# Add attributes and methods to bring the class to life!
# Use constructors to initialize each object with unique values.
A# dd an inheritance layer to explore polymorphism or encapsulation.


# Base class
class Smartphone:
    def __init__(self, brand, model, storage, battery_life):
        """Constructor to initialize a Smartphone object"""
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB
        self.battery_life = battery_life  # in hours
        self._is_power_on = False  # Encapsulation: Protected attribute
    
    def power_on(self):
        """Turns on the smartphone"""
        if not self._is_power_on:
            self._is_power_on = True
            print(f"{self.brand} {self.model} is now ON.")
        else:
            print(f"{self.brand} {self.model} is already ON.")

    def power_off(self):
        """Turns off the smartphone"""
        if self._is_power_on:
            self._is_power_on = False
            print(f"{self.brand} {self.model} is now OFF.")
        else:
            print(f"{self.brand} {self.model} is already OFF.")

    def get_specs(self):
        """Returns the phone's specifications"""
        return f"{self.brand} {self.model}: {self.storage}GB


# Create a program that includes animals or vehicles with the same action (like move()). However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).
# Base class
class Vehicle:
    def move(self):
        """A generic move method to be overridden by subclasses"""
        pass

# Subclass: Car
class Car(Vehicle):
    def move(self):
        print("🚗 Driving on the road...")

# Subclass: Plane
class Plane(Vehicle):
    def move(self):
        print("✈️ Flying in the sky...")

# Subclass: Boat
class Boat(Vehicle):
    def move(self):
        print("🚢 Sailing on the water...")

# Subclass: Bicycle
class Bicycle(Vehicle):
    def move(self):
        print("🚴 Pedaling on the street...")

# Function to demonstrate polymorphism
def test_movement(vehicles):
    for vehicle in vehicles:
        vehicle.move()

# Create instances
car = Car()
plane = Plane()
boat = Boat()
bicycle = Bicycle()

# Test movement
vehicles = [car, plane, boat, bicycle]
test_movement(vehicles)