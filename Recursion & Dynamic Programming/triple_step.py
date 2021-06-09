# A child is running up a staircase with n steps and can hop either 1 step, 2
# steps, or 3 steps at a time. Implement a method to count how many possible
# ways the child can run up the stairs. 
# 
# Hints: #152, #178, #217, #237, #262, #359

# questions

# Solution
# if you knew the number of paths for step (n-1), (n-2) and (n-3), you can
# calculate the number of paths to n: f(n) = f(n-1) + f(n-2) + f(n-3)

# suppose n = 4
# child can go up 
#   1,1,1,1     1,1,2   1,2,1   2,1,1   2,2     3,1     1,3     
# f(1) = 1 = 1
# f(2) = 1,1; 2 = 2
# f(3) = 1,1,1;1,2;2,1;3 = 4
# f(4) = f(1) + f(2) + f(3)

class TripleStep:
    def triple_step_recurse(self, n):
        if n == 0 or n == 1 or n == 2:
            return n
        elif n == 3:
            return 4
        else:
            return self.triple_step_recurse(n-1) + self.triple_step_recurse(n-2) + self.triple_step_recurse(n-3)

    def triple_step_recurse_memo(self, n, memo={}):
        if n in memo:
            return memo[n]
        else:
            if n == 0 or n == 1 or n == 2:
                return n
            elif n == 3:
                return 4
            else:
                memo[n] = self.triple_step_recurse_memo(n-1, memo) + self.triple_step_recurse_memo(n-2, memo) + self.triple_step_recurse_memo(n-3, memo)
                return memo[n]


t = TripleStep()
print(t.triple_step_recurse(20))
print(t.triple_step_recurse_memo(40))