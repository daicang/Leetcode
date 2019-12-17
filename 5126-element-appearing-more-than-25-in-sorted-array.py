class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        threshold = len(arr) / 4
        counter = 0
        last_elem = None
        for elem in arr:
            if elem == last_elem:
                counter += 1
            else:
                last_elem = elem
                counter = 1
            if counter > threshold:
                return elem


s = Solution()
data = [
    [1,2,2,6,6,6,6,7,10],
    [1],
]

for d in data:
    print s.findSpecialInteger(d)
