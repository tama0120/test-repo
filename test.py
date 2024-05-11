import numpy as np

def print_hello():
    print("hello")

arr = np.arange(10)
print("before:", arr)
arr += 1

print("after:", arr)