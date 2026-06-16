class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {}
        def dfs(s, i):
            if i in cache:
                return cache[i]
            if i >= len(s) - 1:
                if i == len(s) - 1 and s[i]=='0':
                    return 0
                return 1
            if int(s[i]) == 0:
                return 0
            
            if int(s[i:i+2])>26:
                cache[i] = dfs(s, i + 1)
                return cache[i]

            cache[i] = dfs(s, i+1) + dfs(s, i+2) 
            return cache[i]


        return dfs(s, 0)
            
            