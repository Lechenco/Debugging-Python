import math
import random

def squareroot(x, eps = 10e-7):
    assert x >= 0
    y = math.sqrt(x)
    assert abs(y * y - x) < eps 
    return y

for i in range(1, 1000):
    r = random.random() * 10000
    z = squareroot(r)

print("Done!")
    
