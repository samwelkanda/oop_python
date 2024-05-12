# COMPOSITION   
class Battery:
    def charge(self):
        return "Battery charging"

class Smartphone:
    def __init__(self):
        self.battery = Battery()

    def charge_phone(self):
        return self.battery.charge()


phone = Smartphone()
print(phone.charge_phone())  # Output: Battery charging