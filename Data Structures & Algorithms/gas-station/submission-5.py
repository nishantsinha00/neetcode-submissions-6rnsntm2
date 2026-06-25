class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        temp = [g - c for g, c in zip(gas, cost)]
        temp += temp
        if sum(temp) < 0:
            return - 1
        print(temp)
        def kadane_with_indices(arr):
            max_ending_here = max_so_far = arr[0]
            start = end = temp_start = 0
            
            for i in range(1, len(arr)):
                if arr[i] > max_ending_here + arr[i]:
                    max_ending_here = arr[i]
                    temp_start = i
                else:
                    max_ending_here += arr[i]
                
                if max_ending_here > max_so_far:
                    max_so_far = max_ending_here
                    start, end = temp_start, i

            return max_so_far, start, end

        mx, ans, end = kadane_with_indices(temp)

        return ans 