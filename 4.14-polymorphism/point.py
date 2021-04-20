class Point:

    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
if __name__ == '__main__':
    # This won't work until you finish implementing the Point class.
    origin = Point()
    point = Point(4, 1)
    other_point = Point(3, -3)
    third_point = point + other_point

    print(point)
    print(other_point)
    print(third_point)
