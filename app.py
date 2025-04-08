class Superhero:
    def __init__(self, name, power, strength_level):
        self.name = name
        self.power = power
        self.__strength_level = strength_level  # Encapsulated attribute

    def display_info(self):
        print(f"{self.name} has the power of {self.power}.")

    def get_strength(self):
        return self.__strength_level

    def train(self):
        self.__strength_level += 10
        print(f"{self.name} trained! Strength is now {self.__strength_level}.")

# Inherited Class
class FlyingHero(Superhero):
    def __init__(self, name, power, strength_level, flight_speed):
        super().__init__(name, power, strength_level)
        self.flight_speed = flight_speed

    def fly(self):
        print(f"{self.name} is flying at {self.flight_speed} mph!")

# Example
hero1 = FlyingHero("SkyStorm", "Wind Control", 80, 300)
hero1.display_info()
hero1.fly()
hero1.train()
