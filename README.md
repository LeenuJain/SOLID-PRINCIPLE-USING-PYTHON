# SOLID-PRINCIPLE-USING-PYTHON
explanation on solid principle with python code

# System Desing
System Design is the process of designing the elements of the system such as **Architecture**, **Modules**, **Components** & different **Interfaces** of those componnents, and **Data Flow** over the system — with the goal of building a system that is **efficient**, **maintainable**, and **scalable**.

### 📌 Key Concepts Explained (with Examples)

| Term                        | Simple Meaning                           | Example (Food Delivery App)                    |
|-----------------------------|-------------------------------------------|------------------------------------------------|
| **Architecture**            | Overall system blueprint                 | Microservices setup, Client-Server design      |
| **Module**                  | Major function area                      | Login, Search, Payment                         |
| **Component**               | Building blocks inside modules           | UPI, Wallet, Card payment components           |
| **Interfaces of Components**| How components talk to each other        | Search takes "pizza" as input, returns results |
| **Data Flow over System**   | How data moves between parts             | User → Search → Restaurant → Payment           |

### 📈 Goals of a Good System

| Term             | Meaning                        | Example in Food App                               |
|------------------|--------------------------------|---------------------------------------------------|
| **Efficient**     | Fast, low resource usage       | Quick search & payment                            |
| **Maintainable**  | Easy to fix or update          | Add new payment method without breaking old ones  |
| **Scalable**      | Grows well under more users    | Handles 1 lakh orders smoothly during a festival  |

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
lets suppose you are having a class CurrencyConverter which converts the INR to Any Currency, also it contains display function.
```python 
class CurrencyConvert:
    def __init__(self, rupees, curr_type):
        self.indian_rupees = rupees
        self.currency_type = curr_type
    
    def currency_convertor(self):
        if self.currency_type == 'Doller':
            in_doller = self.indian_rupees / 94.03
            return in_doller
        elif self.currency_type == 'Yuro':
            in_yuro = self.indian_rupees / 83.00
            return in_yuro
        
    def display_currency(self):
        currency = self.currency_convertor()
        print(f"Converted INR to {self.currency_type}, amount is {currency}")
    
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
class PaymentMethod(ABC):
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
Any Derived class should be able to substitute its parent class without consumer knowing it. The behavior of a subclass should be consistent with the behavior of the parent class. in simple words a subclass or derived class must able to do all the things that a parent class do.LSP is about **behavioral correctness in substitution**.
let's suppose we have a bird class in which two methods are there, one is fly another is eat, now there is two derived classes one is parrot & second is ostrich, so parrot class can perform both fly & eat, but ostrich cannot fly. Here LSP failed.

```python
from abc import ABC, abstractmethod
class Bird(ABC):
    @abstractmethod
    def flyingbird(self):
        pass

    @abstractmethod
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
The Bird base class provides a contract (eating_bird), and both FlyingBirds and NonFlyingBird subclasses implement it appropriately. This ensures that both subclasses can replace the Bird class without breaking any functionality.

Lets consider one more example with real time application. Imagine you're building an e-commerce app (like Amazon or Flipkart), and you support different payment methods: 
- Credit Card
- UPI
- Cash on Delivery (COD)

```python
class Payment:
    def pay(self, amount):
        print(f"Paying ₹{amount}")

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} via Credit Card")

class UPIPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} via UPI")

class CODPayment(Payment):
    def pay(self, amount):
        raise Exception("Can't process COD online!")

def process_payment(payment: Payment):
    payment.pay(500)

process_payment(UPIPayment())        # ✅ Works
process_payment(CreditCardPayment()) # ✅ Works
process_payment(CODPayment())        # ❌ Raises error

```
This breaks LSP. Even though CODPayment is a subclass of Payment, you cannot substitute it safely in place of the parent.
Real-World Consequences: 
- The app crashes if someone tries to use COD through this flow.
- A developer might assume all Payment types are safe to use, but they’re not.
- The interface (pay()) promises something COD cannot deliver

Fixing It with Better Design: 

```python
# Base class (general type)
class Payment:
    pass

# Subclass for online payments only
class OnlinePayment(Payment):
    def pay(self, amount):
        print(f"Processing online payment of ₹{amount}")

# Concrete subclasses that follow LSP
class CreditCardPayment(OnlinePayment):
    def pay(self, amount):
        print(f"Paid ₹{amount} via Credit Card")

class UPIPayment(OnlinePayment):
    def pay(self, amount):
        print(f"Paid ₹{amount} via UPI")

# Separate class for Cash on Delivery
class CODPayment(Payment):
    def confirm_order(self):
        print("Order confirmed. Please pay ₹amount in cash on delivery.")

# Function that works only with OnlinePayment types
def process_online_payment(payment: OnlinePayment, amount):
    payment.pay(amount)

# Function that handles COD orders
def process_cod_order(payment: CODPayment):
    payment.confirm_order()

# ✅ Working correctly
credit_card = CreditCardPayment()
upi = UPIPayment()
cod = CODPayment()

# LSP-compliant usage
process_online_payment(credit_card, 500)   # ✅ OK
process_online_payment(upi, 300)           # ✅ OK

# COD handled separately
process_cod_order(cod)                     # ✅ OK

```
This way:
- COD is not forced to pretend to be an online payment method.
- Only classes that can truly pay online are substituted in this flow.
- LSP is preserved ✅

## Interface Segregation Principle (ISP)
This principle advocates that an interface should only include methods that are relevant to the implementing class. in other words, it goes against Fat or Bulky interfaces in class instead having small interfaces with group of methods each serving a perticular purpose.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_volume(self):
        pass

    @abstractmethod
    def calculate_peri(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

    def calculate_peri(self):
        return 2 * 3.14 * self.radius

    def calculate_volume(self):
        raise NotImplementedError("Circle does not have a volume!")

class Ractangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        return self.breadth * self.length

    def calculate_volume(self):
        raise NotImplementedError("Ractangle does not have Volume!")

    def calculate_peri(self):
        return 2 * (self.length + self.breadth)

if __name__ == '__main__':
    circle = Circle(10)
    area = circle.calculate_area()
    perimeter = circle.calculate_peri()
    print(f"Area : {area} , Perimeter: {perimeter} ")

    ract = Ractangle(10, 20)
    ract.calculate_area()
    ract.calculate_volume()
"""raise NotImplementedError("Ractangle does not have Volume!")
NotImplementedError: Ractangle does not have Volume!"""
```
To Resolve this, instead of making bulky Interface which cover so many things, we can concentrate on making interfaces with group of relevent menthods, like we can interface "Shape" with general purpose, than create two more interfaces like 3d_shapes, 2d_shapes, which contains methods for that only.
Code :

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def display_result(self):
        pass

# Interface for 2D Shapes
class Shape2D(Shape):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

# Interface for 3D Shapes
class Shape3D(Shape):
    @abstractmethod
    def calculate_volume(self):
        pass

    @abstractmethod
    def calculate_surface_area(self):
        pass

class Circle(Shape2D):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius

    def display_result(self):
        print(f"Circle Area : {self.calculate_area()}, Circle Perimeter : {self.calculate_perimeter()}")


class Cube(Shape3D):
    def __init__(self, side):
        self.side = side

    def calculate_volume(self):
        return self.side ** 3

    def calculate_surface_area(self):
        return 6 * (self.side ** 2)

    def display_result(self):
        print(f"Cube Volume : {self.calculate_volume()} , Cube Surface Area : {self.calculate_surface_area()}")


if __name__ == "__main__":
    circle_obj = Circle(10)
    circle_obj.display_result()

    cube_obj = Cube(20)
    cube_obj.display_result()
    
"""
Circle Area : 314.0, Circle Perimeter : 62.800000000000004
Cube Volume : 8000 , Cube Surface Area : 2400
"""
```
Shape2D interface is designed specifically for 2D shapes with methods like calculate_area and calculate_perimeter.
Shape3D interface is designed for 3D shapes with methods like calculate_volume and calculate_surface_area.
Each shape class is responsible for implementing only the methods relevant to its type (2D or 3D), improving modularity and maintainability.

## Dependency Inversion Principle (DIP)
As the name suggest, inverse the dependency i.e. never depend on anything concrete always dependent on interfaces. in simple words high level module should never be dependent on lower level module. they should be dependent on abstraction.
Example:

```python
class CreditCardProcessor:
    def process_payment(self, amount):
        print(f"Processing Credit Card payment of {amount}")

class PaymentService:
    def __init__(self):
        self.processor = CreditCardProcessor()  # Direct dependency

    def make_payment(self, amount):
        self.processor.process_payment(amount)

service = PaymentService()
service.make_payment(1000)
```
The PaymentService is tightly coupled to CreditCardProcessor. Adding new payment types like PayPal would require modifying the PaymentService.
to resolve this check below code:

```python
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

```
you might thinks, whats the differece high level module PaymentService is still dependent on PaymentProcessor, but its not tightly coupled now. Let me clarify why the high-level module (in this case, PaymentService) still depends on the PaymentProcessor abstraction and why this is not considered tight coupling.
- The high-level module doesn't care how the PaymentProcessor implementations work. It only relies on the contract (interface) provided by the PaymentProcessor abstraction.
- Concrete implementations can be swapped in or out without modifying the PaymentService code.
