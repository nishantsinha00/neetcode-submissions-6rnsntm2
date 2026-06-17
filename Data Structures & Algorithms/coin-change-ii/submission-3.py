class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        cache = {}
        def helper(i, a):
            if (i, a) in cache:
                return cache[(i, a)]
            if a == 0:
                cache[(i, a)] = 1
                return cache[(i, a)]

            if a < 0 or i >= n:
                cache[(i, a)] = 0
                return cache[(i, a)]

            ans = helper(i + 1, a)
            
            if a  >= coins[i]:
                ans += helper(i, a - coins[i])

            cache[(i, a)] = ans
            return cache[(i, a)]


        return helper(0, amount)
