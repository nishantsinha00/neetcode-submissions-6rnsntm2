class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0
        for num in nums:
            if num in s:
                s.remove(num)
                l, r = num - 1, num + 1
                tmp = 1
                while (l in s) or (r in s):
                    if r in s:
                        s.remove(r)
                        tmp += 1
                        r += 1
                    if l in s:
                        s.remove(l)
                        tmp += 1
                        l -= 1
                ans = max(tmp, ans)

        return ans
