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

so let's suppose, if u want to add more currency like ("Yen","Pound") than again you need to change on CurrencyCovert class and if u want to update the display method you need to change on CurrencyConvert. which is violating the single responsibility principle. Convertion & Display are two different responsibilites.
Refactored Code :
```python


```

