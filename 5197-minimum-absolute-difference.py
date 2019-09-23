class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()

        diff = None
        pairs = []

        for i in range(1, len(arr)):
            d = arr[i] - arr[i-1]
            if diff is None:
                diff = d
            else:
                diff = min(diff, d)

        for i in range(1, len(arr)):
            d = arr[i] - arr[i-1]
            if d == diff:
                pairs.append([arr[i-1], arr[i]])

        return pairs
