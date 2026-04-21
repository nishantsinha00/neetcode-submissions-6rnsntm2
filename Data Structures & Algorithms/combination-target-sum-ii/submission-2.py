class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        temp = []
        ans = []
        nums = []
        count = {}
        for c in candidates:
            if count.get(c, 0) == 0:
                nums.append(c)
            count[c] = count.get(c, 0) + 1
        def dfs(i, t):
            if t == 0:
                ans.append(temp.copy())
                return
            if t < 0 or i >= len(nums):
                return 
            if count[nums[i]] > 0:
                count[nums[i]] -= 1
                temp.append(nums[i])
                dfs(i, t - nums[i])
                count[nums[i]] += 1
                temp.pop()
            dfs(i + 1, t)
            return

        dfs(0, target)
        return ans
