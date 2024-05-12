""""

Adapter Pattern (Structural)
Purpose: Allows incompatible interfaces to work together.
How It Works: The Adapter pattern acts as a bridge between two incompatible interfaces. This pattern involves a single class, the Adapter, which joins functionalities of independent or incompatible interfaces.
Use Case: Commonly used in software libraries and frameworks, where the functionality provided by a class needs to be made compatible with the rest of the system.
"""

class EuropeanSocketInterface:
    def voltage(self):
        pass


class AmericanSocketInterface:
    def voltage(self):
        pass


class EuropeanSocket(EuropeanSocketInterface):
    def voltage(self):
        return 230


class AmericanSocket(AmericanSocketInterface):
    def voltage(self):
        return 110


class SocketAdapter(EuropeanSocketInterface):
    def __init__(self, socket):
        self.socket = socket

    def voltage(self):
        return self.socket.voltage()


# Usage
american_socket = AmericanSocket()
adapter = SocketAdapter(american_socket)
print(f"Adapter voltage: {adapter.voltage()}V")  # Adapter voltage: 110V