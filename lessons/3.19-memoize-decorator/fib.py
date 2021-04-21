from memoize import memoize

@memoize
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

if __name__ == '__main__':
    fib(10)
    fib(25)
    fib(50)
    fib(100)

