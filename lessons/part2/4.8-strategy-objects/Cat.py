class Cat():
    def __init__(self, name, age, isIndoor=True):
        self.name = name
        self.age = age
        self.isIndoor = isIndoor

    def speak(self):
        print(f'rrr"')
    
    def __repr__(self):
        return f'<{self.name}, {self.age}, {self.isIndoor}>'

