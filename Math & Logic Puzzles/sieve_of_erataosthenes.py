# Sieve of Erathosthenes 
# 
# Have an array from 2 to N. Start with 2 in the array and cross of all
# multiples of 2 until N. Pick the next number 3 and do the same. Repeat this
# process for square root of N elements

import math

class Sieve:
    def list_primes(self, n):
        prime_candidates = list(range(n + 1))
        prime_candidates[1] = 0
        incr = 2
        while incr <= int(math.sqrt(n)):
            for i in range(incr * incr, n + 1, incr):
                prime_candidates[i] = 0
                
            if incr == 2:
                incr += 1
            else:
                incr += 2

        prime_candidates = [num for num in prime_candidates if num != 0]
        print(prime_candidates)

s = Sieve()
s.list_primes(100)