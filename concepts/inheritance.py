# Inheritance

class Animal:
    
    classification: str = "mammal"
    
    def __init__(self, name: str, age: int): # Constructor
        self.name = name # Instance attribute
        self.age = age  # Instance attribute

    @classmethod
    def is_mammal(cls):
        return cls.classification == "mammal"
    
    def speak(self):
        pass
    
    


class Dog(Animal):
    """Represents a dog."""
        
    def speak(self):
        return f"{self.name} says Woof!"
        
    def __str__(self):
        return f"{self.name} is {self.age} years old."
    
    def __repr__(self):
        return f"Dog({self.name}, {self.age}"

class RussellTerrier(Dog):
    """Represents a Russell terrier."""
    
    def run(self):
        return "Russel terrier is fastest"
    

class Bulldog(Dog):
    """Represents a bulldog."""
    
    def __init__(self, name: str, age: int, color: str):
        super().__init__(name, age)
        self.color = color
        
    def __str__(self):
        return f"{self.name} is {self.age} years old and is {self.color}."
    
    def __repr__(self):
        return f"Bulldog({self.name}, {self.age}, {self.color})"

    
    def run(self):
        return "Bulldog is slowest"
    
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age and self.color == other.color
    
