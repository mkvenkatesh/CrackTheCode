# Check if a number is prime

import math
from timeit import Timer

class Prime:
    def is_prime(self, n):
        if (n < 2):
            return False
        for i in range (2, n):
            if n % i == 0:
                return False
        return True

    def is_prime_optimized(self, n):
        if n < 2:
            return False
        elif n % 2 == 0:
            return False
            
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True
                

p = Prime()
print("6 is prime?", p.is_prime(6))
print("7 is prime?", p.is_prime(7))
print("8 is prime?", p.is_prime(8))
print("9 is prime?", p.is_prime(9))
print("10 is prime?", p.is_prime(10))
print("11 is prime?", p.is_prime(11))

t1 = Timer("Prime().is_prime(8191)", "from __main__ import Prime")
t2 = Timer("Prime().is_prime_optimized(8191)", "from __main__ import Prime")

print(t1.timeit(10))
print(t2.timeit(10))

