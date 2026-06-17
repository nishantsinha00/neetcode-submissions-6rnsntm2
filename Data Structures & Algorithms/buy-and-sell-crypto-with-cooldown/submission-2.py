class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        mem = {}
        def helper(i, holding):
            if (i, holding) in mem:
                return mem[(i, holding)]
            if i >= len(prices):
                mem[(i, holding)] =  0
                return mem[(i, holding)]

            if holding:
                mem[(i, holding)] =  max(prices[i] + helper(i + 2, False), helper(i + 1, True))
            else:
                mem[(i, holding)]  = max(helper(i + 1, True) - prices[i], helper(i + 1, False))
            return mem[(i, holding)]

        return helper(0, False)