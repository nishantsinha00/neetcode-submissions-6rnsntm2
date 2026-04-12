class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans  = 0
        minP = prices[0]

        for i in range(1, len(prices)):
            minP = min(prices[i], minP)
            ans = max(prices[i] - minP, ans)

        return ans