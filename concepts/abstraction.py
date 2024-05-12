from abc import ABC, abstractmethod


class AbstractVehicle(ABC):
    @abstractmethod
    def move(self):
        pass


class Car(AbstractVehicle):
    def move(self):
        print("Car is moving")