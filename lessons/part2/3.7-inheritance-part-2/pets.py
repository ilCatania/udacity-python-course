from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @abstractmethod
    def speak(self):
        pass
        
class Cat(Animal):
    isIndoor = True

    def __init__(self, name, age, isIndoor=True):
        """Create a new cat"""
        super().__init__(name, age)
        self.isIndoor = isIndoor

    def speak(self):
        """Make the cat pur"""
        print(f'{self.name} says, "purrrrrr"')
        
        
class Dog(Animal):

    def __init__(self, name:str, age:int, breed:str, weight:int):
        """Create a new dog"""
        super().__init__(name, age)
        self.breed = breed
        self.weight = weight

    def speak(self) -> None:
        """Make the dog bark"""
        print(f'{self.name} says, "woof"')

        
class Frog(Animal):
    
    def __init__(self, name: str, age: int, color):
        super().__init__(name, age)
        self.color = color
        
    def speak(self):
        print("Croak croak!")
        

if __name__ == "__main__":
    wiskers = Cat('Wiskers', 3)
    paws = Dog('Mr. Paws', 4, 'dachshund', 18)
    wiskers.speak()
    paws.speak()
    
    g = Frog("George", 1, "Green")
    g.speak()

