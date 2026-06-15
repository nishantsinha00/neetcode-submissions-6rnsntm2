class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def helper(nums): 
            a = nums[0]
            n = len(nums)
            if n == 1:
                return nums[0]
            b = max(nums[0], nums[1])
        
            ans = b
            for i in range(2, n):
                ans = max(ans, a + nums[i])
                a = b
                b = ans

            return ans

        return max(nums[0], helper(nums[1:]),
                            helper(nums[:-1]))