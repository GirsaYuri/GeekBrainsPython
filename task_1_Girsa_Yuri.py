import random

def rand_gen(n):
    for i in range(1, n + 1, 2):
        yield i

nums_gen = rand_gen(15)

print(next((nums_gen)))
print(next((nums_gen)))
print(next((nums_gen)))