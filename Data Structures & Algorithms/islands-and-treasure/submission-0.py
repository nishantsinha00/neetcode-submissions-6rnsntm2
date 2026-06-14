class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2**31 - 1
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        rows, cols = len(grid), len(grid[0])

        def bfs(row, col):
            q = deque()
            visited = set()
            visited.add((row, col))
            q.append((row, col))
            steps = 0
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    if grid[r][c] == 0:
                        return steps
                    for dx, dy in directions:
                        x, y = r + dx, c + dy

                        if 0 <= x < rows and 0 <= y < cols and grid[x][y] != -1 and (x, y) not in visited:
                            visited.add((x, y))
                            q.append((x, y))
                steps += 1
            return INF



        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == INF:
                    grid[row][col] = bfs(row, col)