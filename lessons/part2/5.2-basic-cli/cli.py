import sys
name = sys.argv[1]
fr = f" from {sys.argv[2]}" if len(sys.argv) > 2 else ""
print(f'hello, {name}{fr}')

