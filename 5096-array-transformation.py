class Solution(object):
    def transformArray(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        import copy

        while True:
            last = copy.copy(arr)
            unchanged = True
            for i in range(len(last)):
                if i in (0, len(arr)-1):
                    continue

                if last[i] < last[i-1] and last[i] < last[i+1]:
                    unchanged = False
                    arr[i] += 1
                elif last[i] > last[i-1] and last[i] > last[i+1]:
                    unchanged = False
                    arr[i] -= 1

            if unchanged:
                return arr


s = Solution()

inputs = [
    [1,6,3,4,3,5],
    [2,1,2,1,1,2,2,1]
]

for i in inputs:
    print s.transformArray(i)

