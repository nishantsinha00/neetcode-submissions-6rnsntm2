class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a, b = 0, 0
        n = len(cost)
        ans = 1e9
        for i in range(2, n + 1):
            ans = min(a + cost[i - 2], b + cost[i- 1])
            a = b
            b = ans

        return ans