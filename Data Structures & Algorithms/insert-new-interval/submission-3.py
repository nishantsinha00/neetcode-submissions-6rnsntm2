import bisect
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        ans = []
        i = 0
        appended = False
        if n==0:
            ans.append(newInterval)
        while i < n:
            if (intervals[i][0] <= newInterval[0] <= intervals[i][1] or intervals[i][0] >= newInterval[0]) and not appended:
                m1 = intervals[i][0] if intervals[i][0] <= newInterval[0] <= intervals[i][1] else newInterval[0]
                while i < n and intervals[i][1] < newInterval[1]:
                    i += 1
                if i == n or newInterval[1] < intervals[i][0]:
                    m2 = newInterval[1]
                else:
                    m2 = intervals[i][1]
                    i += 1
                ans.append([m1, m2])
                appended = True
                if i < n:
                    ans.append(intervals[i])
                i += 1
                continue
                
            ans.append(intervals[i])
            i += 1

        if newInterval[0] > ans[-1][1]:
            ans.append(newInterval)

        return ans