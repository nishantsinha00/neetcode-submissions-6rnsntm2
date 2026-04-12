class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        n = len(s)
        ans = 0
        prev = 0
        for i in range(n):
            if s[i] in mp:
                prev = max(mp[s[i]] + 1, prev)
            mp[s[i]] = i
            ans = max(ans, i - prev + 1)

        return ans
