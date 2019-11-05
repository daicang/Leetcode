class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        gas_rem = []

        for i, g in enumerate(gas):
            gas_rem.append(g-cost[i])

        if sum(gas_rem) < 0:
            return -1

        rem = 0
        start = 0
        for i, val in enumerate(gas_rem):
            rem += val
            if rem < 0:
                # reset start point
                start = i + 1
                rem = 0

        return start


s = Solution()

inputs = [
    [[1,2,3,4,5], [3,4,5,1,2]],
    [[2, 3,4], [3,4,3]],
]

for i in inputs:
    print s.canCompleteCircuit(*i)
