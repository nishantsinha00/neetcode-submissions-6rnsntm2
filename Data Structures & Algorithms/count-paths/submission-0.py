class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        mem = {}
        def helper(i, j):
            if (i, j) in mem:
                return mem[(i, j)]
            if i == m - 1 or j == n -1:
                mem[(i, j)] = 1
                return mem[(i, j)]
            mem[(i, j)] = helper(i + 1, j) + helper(i, j + 1)
            return mem[(i, j)]

        return helper(0, 0)