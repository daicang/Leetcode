
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hand.sort()
        nums = []
        counter = []
        count = 0

        for i, n in enumerate(hand):
            count += 1
            if i == len(hand)-1 or hand[i+1] != n:
                nums.append(n)
                counter.append(count)
                count = 0

        # nums: [1,2,3,4,5]
        # counter: [1,1,2,1,1]

        for i, count in enumerate(counter):
            if count > 0:
                for j in range(i+1, i+groupSize):
                    if j >= len(counter) or counter[j] < count or nums[j] != nums[j-1]+1:
                        return False
                    counter[j] -= count

        return True
