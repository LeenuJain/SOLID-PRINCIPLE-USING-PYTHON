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

ostrich = Ostrich()
ostrich.flyingbird()

