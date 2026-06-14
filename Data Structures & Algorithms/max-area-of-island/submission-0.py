class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        ans = 0

        def bfs(r, c):
            q = deque()
            visited.add((r, c))
            q.append((r, c))
            area = 1
            while q:
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                x, y = q.popleft()
                for dx, dy in directions:
                    row, col = x + dx, y + dy
                    if 0 <= row < rows and 0 <= col < cols and grid[row][col] == 1 and (row, col) not in visited:
                        visited.add((row, col))
                        q.append((row, col))
                        area += 1

            return area


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    ans = max(ans, bfs(r, c))

        return ans
