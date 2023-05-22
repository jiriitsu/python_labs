# pure_python.py
import time
start_time = time.time()
from math import cos, exp
def f(x):
    return cos(x + x * x * x) if x <= 1.0 else exp(-x * x) - x * x + 2.0 * x


def integrate(a, b):
    n = 100_000_000
    h = (b - a) / n
    h2 = h * 0.5
    s = 0.0
    for i in range(n):
        s += f(a + i * h + h2)
    return s * h

if __name__ == '__main__':
    print(integrate(0.0, 2.0))

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
    

