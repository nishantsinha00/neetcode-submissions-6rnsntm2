class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxI = 0
        for i, num in enumerate(nums):
            if i == len(nums) - 1:
                break
            maxI = max(i + num, maxI)
            if maxI <= i:
                print(maxI, i)
                return False
        return maxI >= len(nums) - 1