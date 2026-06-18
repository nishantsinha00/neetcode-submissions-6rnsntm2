class Solution:
    def solve(self, board: List[List[str]]) -> None:
        q = deque()
        m, n = len(board), len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for i in range(n):
            if board[0][i] == "O":
                q.append((0, i))
                board[0][i] = "S"
            if board[m - 1][i] == "O":
                q.append((m - 1, i))
                board[m-1][i] = "S"

        for i in range(1, m - 1):
            if board[i][0] == "O":
                q.append((i, 0))
                board[i][0] = "S"
            if board[i][n - 1] == "O":
                q.append((i, n - 1))
                board[i][n-1] = "S"

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if 0 <= row < m and 0 <= col < n and board[row][col] == "O":
                        board[row][col] = "S"
                        q.append((row, col))

        for i in range(m):
            for j in range(n):
                if board[i][j] == "S":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"


