class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i, j = 0, n - 1
        ans = 0
        while j > i:
            ans = max(ans, min(heights[i], heights[j]) * (j - i))
            if heights[j] >= heights[i]:
                i += 1
            else:
                j -= 1
        return ans