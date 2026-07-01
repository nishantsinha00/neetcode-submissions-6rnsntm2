class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        mp = defaultdict(list)
        for edge in edges:
            mp[edge[0]].append(edge[1])
            mp[edge[1]].append(edge[0])

        visited = set()

        q = deque()
        q.append((0, -1))
        visited.add(0)
        while q:
            for _ in range(len(q)):
                curr, prev = q.popleft()
                for neighbor in mp[curr]:
                    if neighbor in visited:
                        if neighbor == prev:
                            continue
                        else:
                            return False
                    else:
                        q.append((neighbor, curr))
                        visited.add(neighbor)

        return n == len(visited)


        