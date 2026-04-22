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
            if num not in count:
                continue
            cntF = count[num]
            del count[num]
            for i in range(num+1,num + groupSize):
                # print(i, count)
                if (i not in count) or (count[i] < cntF):
                    return False
                count[i] -= cntF
                if count[i] == 0:
                    del count[i]
        return True