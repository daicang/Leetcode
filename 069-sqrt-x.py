class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        def bisearch(left, right):
            if left == right:
                return left
            middle = (left+right) / 2
            pivot = pow(middle, 2)
            if pivot == x:
                return middle
            if pivot < x:
                if pow((middle+1), 2) > x:
                    return middle
                return bisearch(middle+1, right)
            if pow((middle-1), 2) < x:
                return middle-1
            return bisearch(left, middle-1)

        return bisearch(0, x)