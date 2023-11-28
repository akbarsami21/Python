
class Animal:
    def __init__(self,name):
        self.name=name
    def sound(self):
        pass

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print(f"{self.name} sound meow meow")
    
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print(f'{self.name} sound Bow Bow')

c=Cat("Kitty")
c.sound()

d=Dog("Sitty")
d.sound()