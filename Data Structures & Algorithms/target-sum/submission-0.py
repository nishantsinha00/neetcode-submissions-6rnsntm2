class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        def helper(i, target):
            if target == 0 and i == n:
                return 1
            if i >= n:
                return 0

            return helper(i + 1, target - nums[i]) + helper(i + 1, target + nums[i])

        return helper(0, target)