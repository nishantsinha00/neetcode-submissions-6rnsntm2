class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(grid), len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    q.append((row, col))
                    visited.add((row, col))

        ans = 0
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in directions:
                    r, c = x + dx, y + dy
                    if 0<=r<rows and 0<=c<cols and ((r,c) not in visited) and grid[r][c]==1:
                        visited.add((r, c))
                        grid[r][c] = 2
                        q.append((r,c))

            if q:
                ans += 1

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return -1

        return ans

