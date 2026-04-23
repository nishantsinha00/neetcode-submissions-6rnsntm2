class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        temp = []

        def helper(x):
            if len(x) == 1:
                return [[x[0]]]
            ans = []
            for ind in range(len(x)):
                smallAns = [x[ind]]
                largeAns = helper(x[:ind] + x[ind+1:])
                for lAns in largeAns:
                    ans.append(smallAns + lAns)

            return ans

        return helper(nums)
            