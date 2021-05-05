class Cat():
    def __init__(self, name, age, isIndoor=True):
        self.name = name
        self.age = age
        self.isIndoor = isIndoor

    def speak(self):
        print(f'{self.name} says, "purrrrrr"')

herbert = Cat('herbert', 2)
herbert.speak()
