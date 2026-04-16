import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones[:] = [-1 * stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x = -1 * heapq.heappop(stones)
            y = -1 * heapq.heappop(stones)
            newStone = x - y
            if newStone > 0:
                heapq.heappush(stones, y - x)
            
        if len(stones) == 0:
            return 0

        return -1 * stones[0]