class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        n = len(coins)
        def helper(i, target):
            if (i, target) in cache:
                return cache[(i, target)]
            ans = int(1e9)
            if target == 0:
                cache[i, target] = 0
                return cache[(i, target)]
            if i >= n or target <  0:
                cache[(i, target)] = 1e9
                return cache[(i, target)]

            ans = min(ans, helper(i + 1, target), 1 + helper(i, target - coins[i]))
            cache[(i, target)] = ans
            return cache[(i, target)]

        ans = helper(0, amount)
        if ans == 1e9:
            return -1
        return ans


            