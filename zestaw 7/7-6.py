import random

def zeros_ones_repeating():
    flag = False
    while True:
        yield 0 if flag else 1
        flag = not flag

def random_direction():
    directions = ["N", "S", "W", "E"]
    while True:
        yield random.choice(directions)

def days_of_week():
    days = [0, 1, 2, 3, 4, 5, 6]
    index = 0
    while True:
        yield days[index]
        index = (index + 1) % len(days)

def print_iter(iter_func, num=100):
    iterator = iter_func()
    for i in range(num):
        print(next(iterator), end=", " if i % 20 != 19 else "\n")
    print()

# Usage examples
print_iter(zeros_ones_repeating)
print_iter(random_direction)
print_iter(days_of_week)
