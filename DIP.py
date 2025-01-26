from abc import ABC, abstractmethod

# Abstraction
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

# Low-Level Modules
class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing Credit Card payment of {amount}")

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of {amount}")

# High-Level Module
class PaymentService:
    def __init__(self, processor: PaymentProcessor):
        self.processor = processor

    def make_payment(self, amount):
        self.processor.process_payment(amount)

credit_card_service = PaymentService(CreditCardProcessor())
credit_card_service.make_payment(1000)

paypal_service = PaymentService(PayPalProcessor())
paypal_service.make_payment(2000)
