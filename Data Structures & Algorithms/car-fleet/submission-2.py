class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = {}
        ans = len(speed)
        for p, s in zip(position, speed):
            time[p] = (target - p) / s

        position.sort()

        for i in range(len(position) - 1, 0, -1):
            # print(time[position[i]], position[i-1])
            if time[position[i]] >= time[position[i-1]]:
                ans -= 1
                time[position[i-1]] = time[position[i]]

        return ans