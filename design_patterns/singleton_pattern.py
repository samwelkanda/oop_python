"""
Singleton Pattern (Creational)
Purpose: Ensures that a class has only one instance and provides a global point of access to it.

How It Works: The Singleton pattern restricts the instantiation of a class to one object.
It is implemented by creating a class that checks whether an instance of itself already 
exists and creates a new one if it doesn’t.

Use Case: Singleton is often used in configurations, logging, database connections,
file managers where a single point of control is necessary.
"""

class Singleton:
    _instance = None

    @classmethod
    def getInstance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance


# Usage
s1 = Singleton.getInstance()
s2 = Singleton.getInstance()
assert s1 is s2  # Both are the same instance


class Singleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

# Usage
obj1 = Singleton()
obj2 = Singleton()
print(obj1 is obj2)  # Output: True