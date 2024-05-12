"""
Aggregation is a special form of association that represents a “has-a” 
relationship between objects, where child objects can exist independently
of the parent.
"""

class Engine:
    def start(self):
        print("Engine starts")


class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()


engine = Engine()
car = Car(engine)
car.start()  # The Engine is part of the Car, but it's a separate, independent object