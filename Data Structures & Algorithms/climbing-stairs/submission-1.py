
cache = {}
class Solution:
    
    def climbStairs(self, n: int) -> int:

        a, b = 1, 2
        curr = 0
        for i in range(n - 2):
            curr = a + b
            a = b
            b = curr
        return max(curr, n)