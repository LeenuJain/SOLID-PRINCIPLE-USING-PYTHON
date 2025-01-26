from abc import ABC, abstractmethod

class Bird:
    @abstractmethod
    def eating_bird(self):
        pass

class FlyingBirds(Bird):
    def eating_bird(self):
        print(f"Flying Bird Eats")

    def flying_bird(self):
        print(f"Bird Fly")

class NonFlyingBird(Bird):
    def eating_bird(self):
        print("Non Flying bird also eat")

    def running_bird(self):
        print("Non Flying bird run")

parrot = FlyingBirds()
parrot.eating_bird()
parrot.flying_bird()

ostrich = NonFlyingBird()
ostrich.running_bird()
ostrich.eating_bird()