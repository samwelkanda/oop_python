"""
Strategy Pattern (Behavioral)
Purpose: Enables selecting an algorithm’s implementation at runtime.
How It Works: The Strategy pattern involves defining a family of algorithms, encapsulating each one, and making them interchangeable. The algorithm can vary independently from clients that use it.
Use Case: The Strategy pattern is useful in scenarios where you need to dynamically switch algorithms based on context, such as different data compression or encryption methods.
from abc import ABC, abstractmethod
"""
from abc import ABC, abstractmethod

# Strategy Interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Concrete Strategies
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Paid ${amount} using Credit Card."

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Paid ${amount} using PayPal."

# Context
class ShoppingCart:
    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def checkout(self, amount):
        return self.payment_strategy.pay(amount)

# Using Strategy Pattern
credit_card_payment = CreditCardPayment()
paypal_payment = PayPalPayment()

cart1 = ShoppingCart(credit_card_payment)
print(cart1.checkout(100))  # Output: Paid $100 using Credit Card.

cart2 = ShoppingCart(paypal_payment)
print(cart2.checkout(150))  # Output: Paid $150 using PayPal.