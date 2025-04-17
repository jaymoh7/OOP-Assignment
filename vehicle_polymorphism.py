class Vehicle:
    """Base class for all vehicles."""
    
    def __init__(self, name, max_speed):
        """Initialize a vehicle with a name and maximum speed."""
        self.name = name
        self.max_speed = max_speed
        self.current_speed = 0
    
    def start(self):
        """Start the vehicle."""
        return f"{self.name} is starting up."
    
    def stop(self):
        """Stop the vehicle."""
        self.current_speed = 0
        return f"{self.name} has stopped."
    
    def move(self):
        """Move the vehicle. This will be overridden by subclasses."""
        return f"{self.name} is moving."
    
    def accelerate(self, speed_increase):
        """Increase the vehicle's speed."""
        if self.current_speed + speed_increase > self.max_speed:
            self.current_speed = self.max_speed
            return f"{self.name} has reached maximum speed of {self.max_speed} units."
        else:
            self.current_speed += speed_increase
            return f"{self.name} accelerated to {self.current_speed} units."


class Car(Vehicle):
    """Represents a car."""
    
    def __init__(self, name, max_speed, fuel_type):
        """Initialize a car with additional attributes."""
        super().__init__(name, max_speed)
        self.fuel_type = fuel_type
        self.wheels = 4
    
    def move(self):
        """Override the move method for cars."""
        return f"🚗 {self.name} is driving on the road at {self.current_speed} mph."
    
    def honk(self):
        """Car-specific method."""
        return f"🔊 {self.name} goes BEEP BEEP!"


class Boat(Vehicle):
    """Represents a boat."""
    
    def __init__(self, name, max_speed, boat_type):
        """Initialize a boat with additional attributes."""
        super().__init__(name, max_speed)
        self.boat_type = boat_type
    
    def move(self):
        """Override the move method for boats."""
        return f"🚢 {self.name} is sailing across the water at {self.current_speed} knots."
    
    def anchor(self):
        """Boat-specific method."""
        return f"{self.name} has dropped anchor."


class Plane(Vehicle):
    """Represents a plane."""
    
    def __init__(self, name, max_speed, max_altitude):
        """Initialize a plane with additional attributes."""
        super().__init__(name, max_speed)
        self.max_altitude = max_altitude
        self.current_altitude = 0
    
    def move(self):
        """Override the move method for planes."""
        if self.current_altitude > 0:
            return f"✈️ {self.name} is flying through the air at {self.current_speed} mph and altitude of {self.current_altitude} feet."
        else:
            return f"✈️ {self.name} is taxiing on the runway at {self.current_speed} mph."
    
    def take_off(self):
        """Plane-specific method for taking off."""
        if self.current_speed >= 160:
            self.current_altitude = 1000
            return f"{self.name} is taking off! Current altitude: {self.current_altitude} feet."
        else:
            return f"{self.name} needs more speed to take off."
    
    def climb(self, altitude_increase):
        """Increase the plane's altitude."""
        if self.current_altitude == 0:
            return f"{self.name} needs to take off first."
        
        if self.current_altitude + altitude_increase > self.max_altitude:
            self.current_altitude = self.max_altitude
            return f"{self.name} has reached maximum altitude of {self.max_altitude} feet."
        else:
            self.current_altitude += altitude_increase
            return f"{self.name} climbed to {self.current_altitude} feet."


# Demonstrate polymorphism
if __name__ == "__main__":
    # Create different vehicle objects
    sedan = Car("Toyota Camry", 120, "Hybrid")
    yacht = Boat("Sea Breeze", 35, "Sailing Yacht")
    jet = Plane("Boeing 737", 550, 41000)
    
    # Create a list of vehicles to demonstrate polymorphism
    vehicles = [sedan, yacht, jet]
    
    print("=== Starting all vehicles ===")
    for vehicle in vehicles:
        print(vehicle.start())
    
    print("\n=== Accelerating vehicles ===")
    for vehicle in vehicles:
        print(vehicle.accelerate(30))
    
    print("\n=== Moving vehicles (Polymorphism Demo) ===")
    for vehicle in vehicles:
        print(vehicle.move())  # Each vehicle moves in its own way
    
    print("\n=== Vehicle-specific behaviors ===")
    print(sedan.honk())
    print(yacht.anchor())
    print(jet.take_off())  # Not enough speed yet
    
    print("\n=== More acceleration and altitude ===")
    print(jet.accelerate(150))  # Now has enough speed
    print(jet.take_off())
    print(jet.climb(10000))
    
    print("\n=== Final movement status ===")
    for vehicle in vehicles:
        print(vehicle.move())  # Note how the plane's movement description changed