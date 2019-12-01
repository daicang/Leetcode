class Solution(object):
    def numOfBurgers(self, tomatoSlices, cheeseSlices):
        """
        :type tomatoSlices: int
        :type cheeseSlices: int
        :rtype: List[int]
        """
        b1 = (4, 1)
        b2 = (2, 1)

        if (tomatoSlices > 4*cheeseSlices) or tomatoSlices < 2*cheeseSlices or ((tomatoSlices - 2*cheeseSlices) % 2 != 0):
            return []

        tomato = (tomatoSlices - 2*cheeseSlices) / 2
        cheese = (tomatoSlices - tomato*4) / 2

        return [tomato, cheese]

s = Solution()

data = [
    [16, 7],
    [17, 4],
    [4, 17],
    [0, 0],
    [2, 1]
]

for d in data:
    print s.numOfBurgers(*d)

