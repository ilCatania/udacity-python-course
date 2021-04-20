import helper

"""Generate an infinite stream of successively larger random lists."""

def generate_cases():
    i = 0
    while True:
        i += 1
        yield helper.random_list(i)
        
if __name__ == '__main__':
    for case in generate_cases():
        if len(case) > 10:
            break
        print(case)
