class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        for s in strs:
            temp = [0] * 26
            for c in s:
                temp[ord(c) - ord('a')] += 1
            key = tuple(temp)
            if key not in mp:
                mp[key] = []
            mp[key].append(s)
        return list(mp.values())