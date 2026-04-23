import bisect
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        right_max = [height[0]] * n
        left_max = [height[n-1]] * n

        for i in range(1, n):
            right_max[i] = max(right_max[i-1], height[i])

        for i in range(n-2,  -1, -1):
            left_max[i] = max(left_max[i+1], height[i])

        ans = 0

        for i in range(1, n - 1):
            ans += max(min(right_max[i-1], left_max[i+1]) - height[i], 0)

        return ans
