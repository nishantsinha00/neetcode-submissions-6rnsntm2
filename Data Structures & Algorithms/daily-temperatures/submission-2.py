class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        result = [1 for j in range(n)]
        i = 0
        while i < n:
            # if len(stack) == 0 or temperatures[stack[-1]] >= temperatures[i]:
            #     stack.append(i)
            #     i += 1
            #     continue
            while len(stack) > 0 and i < n and temperatures[stack[-1]] < temperatures[i]:
                result[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
            i += 1

        while len(stack) > 0:
            result[stack[-1]] = 0
            stack.pop()  

        return result

            