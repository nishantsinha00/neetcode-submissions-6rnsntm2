class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        n = len(gas)
        if sum(gas) - sum(cost) < 0:
            return -1

        max_ending_here = max_so_far = gas[0] - cost[0]
        start = end = temp_start = 0
        
        for i in range(1,  2 * n):
            i = i % n
            if gas[i] - cost[i] > max_ending_here + gas[i] - cost[i]:
                max_ending_here = gas[i] - cost[i]
                temp_start = i
            else:
                max_ending_here += gas[i] - cost[i]
            
            if max_ending_here > max_so_far:
                max_so_far = max_ending_here
                start, end = temp_start, i

        return start 