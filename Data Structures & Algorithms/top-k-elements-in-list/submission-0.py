class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        ans = []
        cntList = [[] for i in range(len(nums)+1)] 
        for num in nums:
            mp[num] = mp.get(num, 0) + 1
        for key, v in mp.items():
            cntList[v].append(key)
        for x in cntList[::-1]:
            if len(x) == 0:
                continue
            ans += x
            if len(ans) == k:
                return ans
        return [0]