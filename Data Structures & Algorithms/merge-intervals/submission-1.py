class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x: x[0])
        n = len(intervals)
        i = 1
        ans = []
        ans.append(intervals[0])
        while i < n:
            while i < n and ans[-1][1] >= intervals[i][0]:
                ans[-1] = [ans[-1][0], max(intervals[i][1], ans[-1][1])]
                i += 1
            if  i < n:
                ans.append(intervals[i])

            i += 1

        return ans

