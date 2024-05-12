"""
Factory Method Pattern (Creational)
Purpose: Provides an interface for creating objects in a superclass but allows subclasses to alter the type of objects that will be created.
How It Works: The Factory Method pattern works by defining an interface for creating an object but delegates the instantiation to subclasses. This pattern is particularly useful when the process of construction is complex.
Use Case: Creating different UI elements based on user preferences, different payment processing methods based on region.
"""

from abc import ABC, abstractmethod

# Product Interface
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# Concrete Products
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Creator Interface
class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self):
        pass

# Concrete Creators
class DogFactory(AnimalFactory):
    def create_animal(self):
        return Dog()

class CatFactory(AnimalFactory):
    def create_animal(self):
        return Cat()

# Using Factory Method Pattern
dog_factory = DogFactory()
dog = dog_factory.create_animal()
print(dog.speak())  # Output: Woof!

cat_factory = CatFactory()
cat = cat_factory.create_animal()
print(cat.speak())  # Output: Meow!