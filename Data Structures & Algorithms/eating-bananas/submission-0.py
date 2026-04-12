import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def helper(k: int) -> bool:
            total = 0
            for pile in piles:
                total += math.ceil(pile/k)
            if total <= h:
                return True
            return False

        l, r = 1, max(piles)
        ans = r
        while l <= r:
            mid = (l + r) // 2
            if helper(mid):
                ans = min(ans, mid)
                r = mid - 1
            else:
                l = mid + 1

        return ans