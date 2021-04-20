import random

def random_list(size, start=0, stop=10):
    return list(random.randrange(start, stop) for _ in range(size))

