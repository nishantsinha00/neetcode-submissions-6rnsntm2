class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mp = defaultdict(list)
        r_mp = defaultdict(int)
        s = set([i for i in range(numCourses)])

        for p in prerequisites:
            mp[p[1]].append(p[0])
            r_mp[p[0]] += 1
            if p[0] in s:
                s.remove(p[0])

        if len(s) == 0:
            return False

        q = deque(s)

        while(q):
            for _ in range(len(q)):
                curr = q.popleft()
                for nx in mp[curr]:
                    r_mp[nx] -= 1
                    if r_mp[nx] == 0:
                        s.add(nx)
                        q.append(nx)

        return len(s) == numCourses
