import collections


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        c = collections.Counter(nums)
        positive = sorted([x for x in c.keys() if x > 0])
        negative = sorted([x for x in c.keys() if x < 0], reverse=True)

        if 0 in c.keys():
            if c[0] >= 3:
                result.append([0, 0, 0])
            idxp, idxn = 0, 0
            while idxp < len(positive) and idxn < len(negative):
                sum = positive[idxp] + negative[idxn]
                if sum == 0:
                    result.append([positive[idxp], 0, negative[idxn]])
                    idxp += 1
                    idxn += 1
                elif sum < 0:
                    idxp += 1
                else:
                    idxn += 1

        for p in positive:
            for idxn1 in range(len(negative)):
                t1 = p + negative[idxn1]
                if t1 <= 0:
                    break
                start = idxn1 if c[negative[idxn1]] > 1 else idxn1 + 1
                for idxn2 in range(start, len(negative)):
                    t2 = t1 + negative[idxn2]
                    if t2 < 0:
                        break
                    if t2 == 0:
                        result.append([p, negative[idxn1], negative[idxn2]])

        for n in negative:
            for idxp1 in range(len(positive)):
                t1 = n + positive[idxp1]
                if t1 >= 0:
                    break
                start = idxp1 if c[positive[idxp1]] > 1 else idxp1 + 1
                for idxp2 in range(start, len(positive)):
                    t2 = t1 + positive[idxp2]
                    if t2 > 0:
                        break
                    if t2 == 0:
                        result.append([n, positive[idxp1], positive[idxp2]])

        return result


s = Solution()
print s.threeSum([-1, 0, 1, 2, -1, -4])
