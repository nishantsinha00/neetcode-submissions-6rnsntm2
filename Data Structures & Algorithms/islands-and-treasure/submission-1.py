class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2**31 - 1
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()
        rows, cols = len(grid), len(grid[0])

        q = deque()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    visited.add((row, col))
                    q.append((row, col))

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if 0 > row or row == rows or col < 0 or col == cols or grid[row][col] == -1 or (row, col) in visited:
                        continue
                    visited.add((row, col))
                    grid[row][col] = 1 + grid[r][c]
                    q.append((row, col))
