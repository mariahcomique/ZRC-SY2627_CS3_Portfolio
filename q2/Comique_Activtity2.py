#Single Inheritance
class Animal:
    def __init__(self, name):
        self._name = name 

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def make_sound(self):
        print(f"{self._name} makes a generic sound.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self._breed = breed

    def get_breed(self):
        return self._breed

    def set_breed(self, breed):
        self._breed = breed

    def make_sound(self):
        print(f"{self.get_name()} the {self._breed} barks: Woof! Woof!")


print("--- Single Inheritance ---")
dog1 = Dog("Buddy", "Golden Retriever")

dog1.make_sound()

print("\n[Modifying dog1's details]")
dog1.set_name("Holly")
dog1.set_breed("Labrador")
dog1.make_sound()
print(f"Updated Name: {dog1.get_name()}, Breed: {dog1.get_breed()}")
#haha "buddy" and "holly", get it? (weezer reference)

#Multilevel Inheritance
class LivingBeing:
    def __init__(self, kingdom):
        self._kingdom = kingdom

    def get_kingdom(self):
        return self._kingdom

    def set_kingdom(self, kingdom):
        self._kingdom = kingdom


class Animal(LivingBeing):
    def __init__(self, kingdom, name):
        super().__init__(kingdom)
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name


class Dog(Animal):
    def __init__(self, kingdom, name, breed):
        super().__init__(kingdom, name)
        self._breed = breed

    def get_breed(self):
        return self._breed

    def set_breed(self, breed):
        self._breed = breed

    def display_info(self):
        print(f"Kingdom: {self.get_kingdom()} | Name: {self.get_name()} | Breed: {self._breed}")


print("\n--- Multilevel Inheritance ---")
dog1 = Dog("Animalia", "Fita", "Daschund")
dog2 = Dog("Animalia", "Noodle", "Poodle")

dog1.display_info()
dog2.display_info()

print("\n[Adding a new object and modifying values]")
dog3 = Dog("Animalia", "Unknown", "Newfie")
dog3.set_name("Fuwa")
dog3.display_info()

#Hierarchical Inheritance
class Shape:
    def __init__(self, color):
        self._color = color

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    def display_color(self):
        print(f"Color: {self._color}")


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self._radius = radius

    def get_radius(self):
        return self._radius

    def set_radius(self, radius):
        self._radius = radius

    def calculate_area(self):
        return 3.14159 * (self._radius ** 2)


class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self._width = width
        self._height = height

    def get_dimensions(self):
        return self._width, self._height

    def set_dimensions(self, width, height):
        self._width = width
        self._height = height

    def calculate_area(self):
        return self._width * self._height


print("\n--- Hierarchical Inheritance ---")
c1 = Circle("Red", 5)
r1 = Rectangle("Blue", 4, 6)

print(f"Circle Color: {c1.get_color()}, Radius: {c1.get_radius()}, Area: {c1.calculate_area():.2f}")
print(f"Rectangle Color: {r1.get_color()}, Area: {r1.calculate_area()}")

print("\n[Modifying object properties]")
c1.set_color("Purple")
c1.set_radius(10)
print(f"Updated Circle Color: {c1.get_color()}, New Radius: {c1.get_radius()}, New Area: {c1.calculate_area():.2f}")