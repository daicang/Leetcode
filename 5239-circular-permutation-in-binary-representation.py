class Solution(object):
    def circularPermutation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: List[int]
        """
        permutaion = []
        last = [start]

        def alter_bit_len(position):
            if position < 0:
                permutaion.append(last[0])
                return

            alter_bit_len(position-1)
            mask = 1 << position
            last[0] ^= mask
            alter_bit_len(position-1)

        alter_bit_len(n-1)

        return permutaion

tests = [
    [2, 0],
    [2, 3],  # 3,2,0,1
    [3, 2]  # [2,6,7,5,4,0,1,3]
]

s = Solution()

for t in tests:
    print s.circularPermutation(*t)
