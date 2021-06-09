# Fibonacci
# 0, 1, 1, 2, 3, 5, 8, 13, 21 ...
# fib(n) = fib(n-1) + fib(n-2)
# fib(0) = 0 and fib(1) = 1 <-- base case

class Fibonacci:
    def fib_recursion(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib_recursion(n-1) + self.fib_recursion(n-2)

    # top down dynamic programming
    def fib_recursion_with_memoization(self, n, memo={}):
        if n in memo:
            return memo[n]
        else:
            if n == 0:
                return 0
            elif n == 1:
                return 1
            else:
                memo[n] = self.fib_recursion_with_memoization(n-1, memo) + self.fib_recursion_with_memoization(n-2, memo)
                return memo[n]

    # bottom-up dynamic programming
    def fib_bottom_up(self, n, memo={}):
        if n == 0 or n == 1:
            return n
        else:
            memo[0] = 0
            memo[1] = 1
            for i in range(2, n):
                memo[i] = memo[i-1] + memo[i-2]
            return memo[n-1] + memo[n-2]

f = Fibonacci()

for i in range(10):
    print(f.fib_recursion(i))

for i in range(10):
    print(f.fib_recursion_with_memoization(i))    


print(f.fib_recursion(15))
print(f.fib_recursion_with_memoization(35))    
print(f.fib_bottom_up(35))    