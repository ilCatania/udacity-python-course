"""A cat module."""

class Cat():
    """A Cat."""

    def __init__(self, name:str, age:int):
        """Initialize the guy."""
        self.name = name
        self.age = age

    def speak(self) -> None:
        """Let the guy speak.

        >>> kitty.speak()
        Spot says, purrrrrr.
        """
        print(f'{self.name} says, purrrrrr.')


if __name__ == "__main__":
    import doctest
    doctest.testmod(extraglobs={'kitty': Cat('Spot', 3)})
