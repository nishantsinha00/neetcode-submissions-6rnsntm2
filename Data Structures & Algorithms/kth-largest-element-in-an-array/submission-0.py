import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        x =  heapq.nlargest(k, nums)
        return x[-1]