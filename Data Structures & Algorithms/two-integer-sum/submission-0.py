class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        n = len(nums)
        for i in range(n):
            if target - nums[i] in mp:
                return [mp[target - nums[i]], i]
            mp[nums[i]] = mp.get(nums[i], i)
            
        return [0,0]

        