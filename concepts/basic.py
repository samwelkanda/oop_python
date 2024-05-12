from __future__ import annotations

class Point:
    """Represents a point in 2-D space."""
    
    def __init__(self, x: float = 0, y: float =0):
        self.x = x
        self.y = y
        
p1 = Point()
print(p1)

p1.x = 3.0
p1.y = 4.0
print(p1.x)
print(p1.y)

# shallow copy

import copy
p2 = copy.copy(p1)
print(p1 is p2)
        
        
class Rectangle:
    """Represents a rectangle."""
    
    def __init__(self, width: float = 0, height: float = 0, corner: Point = Point()):
        self.width = width
        self.height = height
        self.corner = corner
        
    def __str__(self):
        return f"Width: {self.width}, Height: {self.height}, Corner: ({self.corner.x}, {self.corner.y})"
    
    def area(self) -> float:
        return self.width * self.height
    
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)
    
    def flip(self):
        self.width, self.height = self.height, self.width
        
    def contains(self, point: Point) -> bool:
        return self.corner.x <= point.x < self.corner.x + self.width and self.corner.y <= point.y < self.corner.y + self.height
    
    def grow(self, dwidth: float, dheight: float):
        self.width += dwidth
        self.height += dheight
        
    def move(self, dx: float, dy: float):
        self.corner.x += dx
        self.corner.y += dy
        
    def intersection(self, other: Rectangle) -> Rectangle:
        x = max(self.corner.x, other.corner.x)
        y = max(self.corner.y, other.corner.y)
        width = min(self.corner.x + self.width, other.corner.x + other.width) - x
        height = min(self.corner.y + self.height, other.corner.y + other.height) - y
        return Rectangle(width, height, Point(x, y))
    
    def union(self, other: Rectangle) -> Rectangle:
        x = min(self.corner.x, other.corner.x)
        y = min(self.corner.y, other.corner.y)
        width = max(self.corner.x + self.width, other.corner.x + other.width) - x
        height = max(self.corner.y + self.height, other.corner.y + other.height) - y
        return Rectangle(width, height, Point(x, y))
    
    def __eq__(self, other):
        return self.width == other.width and self.height == other.height and self.corner.x == other.corner.x and self.corner.y == other.corner.y
    
    def __ne__(self, other):
        return not self == other
        
box = Rectangle(100.0, 200.0, Point(0.0, 0.0))
                
# # shallow copy
box2 = copy.copy(box)
print(box2 is box)
print(box2.corner is box.corner)    

# # deep copy
box3 = copy.deepcopy(box)
print(box3 is box)
print(box3.corner is box.corner)


# Using `@classmethod` as a Factory
class Person:
    def __init__(self, name):
        self.name = name

    @classmethod
    def from_full_name(cls, full_name):
        name = full_name.split()[0]
        return cls(name)

# from_full_name is a class method that creates an instance of Person using a full name
john = Person.from_full_name("John Doe")
print(john.name)  # Output: John