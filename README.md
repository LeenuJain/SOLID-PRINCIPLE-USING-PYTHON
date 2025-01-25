# SOLID-PRINCIPLE-USING-PYTHON
explanation on solid principle with python code

# System Desing
System Design is the process of designing the elements of the system such as Architecture, Module, Components & different interfaces of those componnents, and Data flow over the system.
the goal is the create system which is efficient, maintainable & scalable.

## Types of System Design
1. LLD (Low Level Design)
2. HLD (High Level Design)

# High Level Design Vs Low Level Design:
HLD provides the overview or blueprint of the entire system. It gives a bird's-eye view and defines the major components, their relationships, and how they interact with each other.
Think of it like this: If you want to build a house, the engineer will first give you a high-level plan. This plan shows where the kitchen, bedroom, and bathroom will be and how they are connected. It helps you understand the overall structure of the house and how you will move around in it..
At this stage, they don’t go into the finer details, like what materials will be used for the walls or which type of wood will be used for the bed. That detailed planning comes later during the low-level design (LLD) phase. HLD focuses on the big picture but LLD focuses on component level.

# SOLID Principle
While High-Level Design (HLD) focuses on the architecture and components of the system, LLD deals with the detailed design of classes, methods, and interactions within those components—and this is where SOLID principles shine.The SOLID principles are a set of five design principles for writing maintainable and understandable software. They were introduced by Robert C. Martin (also known as Uncle Bob) and have become a cornerstone of object-oriented design and software architecture. The SOLID principles provides guidelines to create well-structured, maintainable, and scalable code at the implementation level.

## The SOLID acronym stands for :
1. Single Responsibility Principle (SRP)
2. Open-Closed Principle (OCP)
3. Liskov Substitution Principle (LSP)
4. Interface Segregation Principle (ISP)
5. Dependency Inversion Principle (DIP)

## Single Responsibility Principle (SRP)
This SRP states that **“A class should have only one reason to change”** which means every class should have a single responsibility or sigle purpose. 
following SRP makes your code more moduler,maintainable and easy to extend. for example. 
lets suppose you are having a class CurrencyConverter which converts the Any Currency to INR. also it contains display function.
```python 
class CurrencyConvert:
    def __init__(self, rupees, curr_type):
        self.indian_rupees = rupees
        self.currency_type = curr_type
    
    def currency_convertor(self):
        if self.currency_type == 'Doller':
            in_doller = self.indian_rupees / 94.03
            return in_doller, self.currency_type
        elif self.currency_type == 'Yuro':
            in_yuro = self.indian_rupees / 83.00
            return in_yuro, self.currency_type
        
    def display_currency(self):
        currency, type = self.currency_convertor()
        print(f"Converted INR to {type}, amount is {currency}")
    
doller_money = CurrencyConvert(1023000, 'Doller')
doller_money.display_currency()

doller_money = CurrencyConvert(1023000, 'Yuro')
doller_money.display_currency()
```
### Whats Wrong Here ? 
The CurrencyConvert class has multiple responsibilities:
1. Conversion Logic: It handles the actual conversion of Indian Rupees to different currencies.
2. Displaying Output: It handles printing the converted values.

so let's suppose, if u want to add more currency like ("Yen","Pound") than again you need to change on CurrencyCovert class and if u want to update the display method you need to change on CurrencyConvert again. which is violating the single responsibility principle.
Refactored Code :

```python
class CurrencyConvertor:
    def __init__(self, rupees, curr_type):
        self.rupees = rupees
        self.currency_type = curr_type
        self.rates = {
            'Doller': 94.03,
            'Yuro': 83.00,
            'Yen': 45.67
        }

    def currency_convertor(self):
        converted = self.rupees / self.rates[self.currency_type]
        return converted, self.currency_type


class DisplayCurrency:
    @staticmethod
    def display_currency(convert_object):
        # Access the instance method of CurrencyConvertor
        converted, curr_type = convert_object.currency_convertor()
        print(f"Converted INR to {curr_type}, amount is {converted}")


# create object & call
convert_object = CurrencyConvertor(10000, 'Doller')
DisplayCurrency.display_currency(convert_object)

```
Now, we can see each class (CurrencyConverteror, DisplayCurrency) both doing single task, if its currency conversion its doing only currency conversion & Display class only display the result.

## Open-Closed Principle (OCP)
An Entity (Class, Module, Method etc) is open for extension but closed for modification. that means you are free to add new functionality but you can not modify the existing code. in simple words extend the existing code, means add new code instead of changing the existing code.
Example : 
let's suppose, we are having an payment class in which different payment methods are implemented, in future we want to add Debit Card payment method, so for adding that we need to update the payment method by adding another if else condition, for that we gonna modify existing code, which violate the Open closed principle.

```python
# open closed principle
class PaymentMethod:
    def make_payment(self, pay_type, amount):
        if pay_type == 'UPI':
            print(f"Payment {amount} done on UPI")
        elif pay_type == 'Net Banking':
            print(f"Payment {amount} done on Net Banking")
        elif pay_type == 'Credit Card':
            print(f"Payment {amount} done on Credit Card")
        else:
            print(f"Unsupported Payment Method")

if __name__ == "__main__":
    payment_obj = PaymentMethod()
    payment_obj.make_payment("Credit Card", 10000)
```
To resolve this, we gonna use abstract method, Abstract method has no implementation.

```python
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
```
You might think, The code looks pretty big now, but even if you want to add another method now, you dont need to change anything in existing code. just create a new class and simply create its object.

## Liskov Substitution Principle (LSP)
Any Derived class should be able to substitute its parent class without consumer knowing it. The behavior of a subclass should be consistent with the behavior of the parent class. in simple words a subclass or derived class must able to do all the things that a parent class do.
let's suppose we have a bird class in which two methods are there, one is fly another is eat, now there is two derived classes one is parrot & second is ostrich, so parrot class can perform both fly & eat, but ostrich cannot fly. Here LSP failed.

```python
from abc import ABC, abstractmethod
class Bird:
    @abstractmethod
    def flyingbird(self):
        pass

    def eatingbird(self):
        pass

class Parrot(Bird):
    def flyingbird(self):
        print("Parrot Can fly")

    def eatingbird(self):
        print("Parrot Can Eat")

class Ostrich(Bird):
    def eatingbird(self):
        print(f"Ostrich Can Eat")

parrot = Parrot()
parrot.flyingbird()
parrot.eatingbird()

ostrich = Ostrich()
ostrich.eatingbird()
ostrich.flyingbird()
```
This code violates the Liskov Substitution Principle (LSP) because the subclass Ostrich does not fully implement the functionality defined in the parent class Bird. Specifically, the flyingbird() method is not implemented for Ostrich. While the code may still work in some cases, it can lead to unexpected issues, particularly when polymorphism is involved.
To resolve this we need to think of a better architecture, like bird class as generalized, we can create sepearate class of flyingbirds and nonflyingbirds, than derive classes like parrot & ostrich.

![image](https://github.com/user-attachments/assets/e2156e17-f13e-49d8-8c4b-159d2d3bce65)

```python
from abc import ABC, abstractmethod

class Bird(ABC):
    @abstractmethod
    def eating_bird(self):
        pass

class FlyingBird(Bird):
    def eating_bird(self):
        print("Flying Bird Eats")

    def flying_bird(self):
        print("Flying Bird Flies")

class NonFlyingBird(Bird):
    def eating_bird(self):
        print("Non-Flying Bird Eats")

    def running_bird(self):
        print("Non-Flying Bird Runs")

parrot = FlyingBird()
parrot.eating_bird()    # Output: Flying Bird Eats
parrot.flying_bird()    # Output: Flying Bird Flies

ostrich = NonFlyingBird()
ostrich.eating_bird()   # Output: Non-Flying Bird Eats
ostrich.running_bird()  # Output: Non-Flying Bird Runs
```
