class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize > 0:
            return False

        count = {}
        unique = sorted(list(set(hand)))

        for h in hand:
            count[h] = count.get(h, 0) + 1

        for num in unique:
            if count[num] == 0:
                continue
            cntF = count[num]
            count[num] = 0
            for i in range(num+1,num + groupSize):
                if (i not in count) or (count[i] < cntF):
                    return False
                count[i] -= cntF

        return True