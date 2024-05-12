"""
Proxy Pattern (Structural)
Purpose: Provides a surrogate or placeholder for another object to control access to it. This is useful for lazy loading, controlling access, or logging, among other things.
How It Works: In the Proxy pattern, a proxy object is used to interface with the real object. The proxy can intercept calls to the real object, adding additional actions like lazy initialization, access control, or logging.
Use Case: The Proxy pattern is widely used in networked applications to add a layer between clients and servers (e.g., to handle remote method invocation). It’s also useful in scenarios where object creation is resource-intensive, and you want to delay it until the object is actually needed.
"""

class Image:
    def display(self):
        pass


class RealImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.load_from_disk()

    def load_from_disk(self):
        print(f"Loading {self.filename}")

    def display(self):
        print(f"Displaying {self.filename}")


class ProxyImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.real_image = None

    def display(self):
        if self.real_image is None:
            self.real_image = RealImage(self.filename)
        self.real_image.display()


# Usage
image = ProxyImage("test_image.jpg")
image.display()  # Loads and displays image
image.display()  # Only displays image, as it's already loaded