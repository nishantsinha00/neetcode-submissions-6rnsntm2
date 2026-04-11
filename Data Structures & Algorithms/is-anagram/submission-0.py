class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp_s = {}
        mp_t = {}

        for char in s:
            if mp_s.get(char, 0) == 0:
                mp_s[char] = 1
            else:
                mp_s[char] += 1

        for char in t:
            if mp_t.get(char, 0) == 0:
                mp_t[char] = 1
            else:
                mp_t[char] += 1

        return mp_s == mp_t