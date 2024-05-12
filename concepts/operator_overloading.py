from __future__ import annotations

class Book:
    """Represents a book."""
    
    def __init__(self, title: str, author: str, pages: int = 0):
        self.title = title
        self.author = author
        self.pages = pages
        
    def __str__(self):
        return f"{self.title} by {self.author} with {self.pages} pages."
    
    # Returns the length of the container. 
    def __len__(self):
        return self.pages
    
    # Equality (==). Checks if two objects are equal.
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    # Operator overloading
    def __del__(self):
        print(f"The book {self.title} has been deleted.")
        
book1 = Book("1984", "George Orwell")
book2 = Book("1984", "George Orwell")
print(book1 == book2)
print(len(book1))
del book1
print(book1)



class Time:
    """Represents the time of day.
    attributes = ["hour", "minute", "second"]
    """
    def __init__(self, hour: int = 0, minute: int = 0, second: int = 0):
        self.hour = hour
        self.minute = minute
        self.second = second
        
    # Returns a user-friendly string representation of the object.
    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"
    
    # return an unambiguous string representation of the object
    def __repr__(self) -> str:
        return f"Time({self.hour}, {self.minute}, {self.second})"
    
    # Addition (+)
    def __add__(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return Time.int_to_time(seconds)
        
    def time_to_int(self) -> int:
        """Converts a time object to seconds."""
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    @staticmethod
    def int_to_time(seconds: int) -> Time:
        """Converts seconds to a time object."""
        time = Time()
        minutes, time.second = divmod(seconds, 60)
        time.hour, time.minute = divmod(minutes, 60)
        return time

    @staticmethod
    def valid_time(time: Time) -> bool:
        """Checks if a time object is valid."""
        if time.hour < 0 or time.minute < 0 or time.second < 0:
            return False
        if time.minute >= 60 or time.second >= 60:
            return False
        return True

    def add_time(t1: Time, t2: Time) -> Time:
        """Adds two time objects."""
        assert Time.valid_time(t1) and Time.valid_time(t2)
        seconds = t1.time_to_int(t1) + t2.time_to_int(t2)
        return Time.int_to_time(seconds)
    
    def is_after(self, other: Time) -> bool:
        """Checks if a time object is after another time object."""
        assert Time.valid_time(self) and Time.valid_time(other)
        return self.time_to_int() > other.time_to_int()
    
start = Time(9, 45, 0)
print(start)
print(repr(start))