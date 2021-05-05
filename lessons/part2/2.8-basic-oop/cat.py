# @TODO create a cat class

class Cat:
    def __init__(self, name: str, age: int, isIndoor: bool = True):
        self.name = name
        self.age = age
        self.isIndoor = isIndoor

    def speak(self):
        print(f"{self.name} says purrrrr")
        
herbert = Cat('Herbert', 2)
herbert.speak()
