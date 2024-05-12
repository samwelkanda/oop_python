# Encapsulation
class Computer:
    def __init__(self, brand: str, model: str, price: float):
        self.__brand = brand
        self.__model = model
        self.__price = price
        self.__number_of_units = 0
        
    @property
    def brand(self):
        return self.__brand
    
    @property
    def model(self):
        return self.__model
    
    @property
    def price(self):
        return self.__price
    
    @brand.setter
    def set_brand(self, brand: str):
        self.__brand = brand
        
    @model.setter
    def set_model(self, model: str):
        self.__model = model
    
    @price.setter
    def set_price(self, price: float):
        self.__price = price
        
    @property
    def number_of_units(self):
        return self.__number_of_units
    
    @number_of_units.setter
    def set_number_of_units(self, number_of_units: int):
        self.__number_of_units = number_of_units
        
    def sell(self, units: int):
        if units <= self.__number_of_units:
            self.__number_of_units -= units
            print(f"{units} units sold")
        else:
            print("Not enough units to sell")
            
class BankAccount:
    def __init__(self, account_holder, balance):
        self._account_holder = account_holder  # Protected attribute
        self.__balance = balance               # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

# Using Encapsulation
account = BankAccount("Alice", 1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())  # Output: 1300