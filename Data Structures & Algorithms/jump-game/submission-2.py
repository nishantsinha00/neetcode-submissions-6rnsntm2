class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxI = 0
        for i, num in enumerate(nums):
            maxI = max(i + num, maxI)
            if maxI <= i and i < len(nums) - 1:
                return False
        return maxI >= len(nums) - 1