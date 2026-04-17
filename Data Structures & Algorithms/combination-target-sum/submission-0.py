class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        def dfs(target, i):
            if target == 0:
                res.append(subset.copy())
                return
            if target < 0:
                return

            if i == len(nums):
                return

            subset.append(nums[i])
            dfs(target - nums[i], i)
            subset.pop()
            dfs(target, i + 1)

        dfs(target, 0)
        return res