
cache = {}
class Solution:
    
    def climbStairs(self, n: int) -> int:
        if n == 0:
            cache[0] = 0
            return 0

        if n == 1:
            cache[1] = 1
            return 1
        
        if n == 2:
            cache[2] = 2
            return 2

        if n - 1 not in cache:
            cache[n-1] = self.climbStairs(n - 1)

        if n - 2 not in cache:
            cache[n-2] = self.climbStairs(n - 2)


        return cache[n-1] + cache[n-2]