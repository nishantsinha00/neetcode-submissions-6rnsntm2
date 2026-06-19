class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        currMin, currMax = 1, 1

        for num in nums:
            tmp = num * currMax
            currMax = max(num, num * currMax, num * currMin)
            currMin = min(tmp, num * currMin, num)
            res = max(res, currMax)

        return res