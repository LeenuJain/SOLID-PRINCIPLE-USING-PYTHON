from abc import ABC, abstractmethod
class PaymentMethod:
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Payment {amount} done on Credit Card")

class UPIPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Payment {amount} done on UPI")

class NetBankingPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Payment {amount} done on Net Banking")

class PaymentProcessor:
    def __init__(self, payment_method):
        self.payment_method = payment_method

    def process_payment(self, amount):
        self.payment_method.pay(amount)


if __name__ == "__main__":
    payment = CreditCardPayment()
    test = PaymentProcessor(payment)
    test.process_payment(10000)

"""
Now its easy to add any other payment method. link crypto or debit card payments....
"""