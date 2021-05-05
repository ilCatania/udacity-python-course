class Dog():

    def __init__(self, name:str, age:int,
                 breed:str, weight:int):
        """Create a new dog"""
        self.breed = breed
        self.weight = weight
        self.name = name
        self.age = age

    def speak(self) -> None:
        """Make the dog bark"""
        print(f'{self.name} says, "woof"')
        
    def __eq__(self, other):
        return self.age == other.age
    
    def __gt__(self, other):
        return self.age > other.age
    
    def __str__(self):
        return self.name

    @classmethod
    def spawn(cls, name:str, parent1, parent2):
        breed = parent1.breed if parent1.breed == parent2.breed else "mixed"
        return cls(name, 0, breed, (parent1.weight + parent2.weight)/20)
    
if __name__ == "__main__":
    sally = Dog('Sally', 6, 'chihuahua', 7)
    henry = Dog('Henry', 7, 'terrier', 15)
    trixy = Dog.spawn('Trixy', sally, henry)
    print(trixy.breed)
