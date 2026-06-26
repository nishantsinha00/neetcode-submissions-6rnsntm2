class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        mp = defaultdict(list)
        r_mp = defaultdict(int)
        s = set([i for i in range(numCourses)])

        for p in prerequisites:
            mp[p[1]].append(p[0])
            r_mp[p[0]] += 1
            if p[0] in s:
                s.remove(p[0])

        ans = list(s)
        if len(s) == 0:
            return []

        q = deque(s)

        while(q):
            for _ in range(len(q)):
                curr = q.popleft()
                for nx in mp[curr]:
                    r_mp[nx] -= 1
                    if r_mp[nx] == 0:
                        ans.append(nx)
                        q.append(nx)

        if len(ans) < numCourses:
            return []

        return ans