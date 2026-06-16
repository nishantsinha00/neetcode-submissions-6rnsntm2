class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {}
        def dfs(text1, text2, x, y):
            ans = 0
            if x == len(text1) or y == len (text2):
                return 0
            if (x, y) in cache:
                return cache[(x, y)]
            if text1[x] == text2[y]:
                ans = max(ans, 1 + dfs(text1, text2, x + 1, y + 1))
            else:
                ans = max(ans, dfs(text1, text2, x, y + 1), dfs(text1, text2, x + 1, y))
            cache[(x, y)] = ans
            return ans

        return dfs(text1, text2, 0, 0)


