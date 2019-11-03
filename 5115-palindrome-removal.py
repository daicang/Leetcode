class Solution(object):
    def minimumMoves(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        size = len(arr)
        dp_cache = []
        for _ in range(size):
            dp_cache.append([None] * size)

        def solve(begin, end):
            if begin > end:
                return 0

            if begin == end:
                return 1

            if dp_cache[begin][end] is not None:
                return dp_cache[begin][end]

            result = solve(begin, end-1) + 1

            for i in range(begin, end):
                if arr[i] == arr[end]:
                    part1 = solve(begin, i-1)
                    part2 = solve(i+1, end-1)
                    if i == end-1:
                        addon = 1
                    else:
                        addon = 0

                    result = min(result, part1+part2+addon)

            dp_cache[begin][end] = result
            return result

        return solve(0, size-1)



s = Solution()

inputs = [
    [1,2],  # 2
    [1,1],
    [1,3,4,1,5], # 3
]

for i in inputs:
    print s.minimumMoves(i)
