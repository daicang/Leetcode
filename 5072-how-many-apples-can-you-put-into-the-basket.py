class Solution(object):
    def maxNumberOfApples(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr.sort()
        left = 5000
        count = 0

        for weight in arr:
            if left < weight:
                break
            left -= weight
            count += 1
        return count

