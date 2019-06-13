import math
from functools import reduce

def lcm(num):
    return reduce(lambda a, b :(a * b) // math.gcd(a, b), list(range(1, num + 1)))

print(lcm(20))
