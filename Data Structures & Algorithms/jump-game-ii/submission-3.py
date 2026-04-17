class Solution:
    def jump(self, nums: List[int]) -> int:
            maxI = nums[0]
            curr = nums[0]
            ans = 0
            for i in range(1, len(nums)):
                curr -= 1
                maxI = max(maxI, i + nums[i])
                if curr == 0 or i == len(nums) - 1:
                    ans += 1
                    curr = maxI - i

            return ans