class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        cache = dict()
        def helper(i, target):
            if (i, target) in cache:
                return cache[(i, target)]
            if target == 0 and i == n:
                return 1
            if i >= n:
                return 0

            cache[(i, target)] = helper(i + 1, target - nums[i]) + helper(i + 1, target + nums[i])
            return cache[(i, target)]

        return helper(0, target)