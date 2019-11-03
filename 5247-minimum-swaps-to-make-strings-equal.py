class Solution(object):
    def minimumSwap(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        x_y_pair = y_x_pair = 0
        size = len(s1)
        for i in range(size):
            if s1[i] == 'x' and s2[i] == 'y':
                x_y_pair += 1
            elif s1[i] == 'y' and s2[i] == 'x':
                y_x_pair += 1

        if (x_y_pair + y_x_pair) % 2 != 0:
            return -1

        swaps = x_y_pair/2 + y_x_pair/2
        if x_y_pair % 2 != 0:
            swaps += 2

        return swaps

s = Solution()

inputs = [
    ['xx', 'yy'],
    ['xy', 'yx'],
    ['xx', 'xy'],
    ["xxyyxyxyxx", "xyyxyxxxyx"],
]

for i in inputs:
    print s.minimumSwap(*i)
