class Solution(object):
    def kthSmallest(self, matrix, k):
        import bisect

        def _get_order1(row, key):
            l = len(row)
            if l == 0:
                return 0
            if l == 1:
                return 1 if row[0] <= key else 0
            if row[l/2] <= key:
                return l/2+1 + _get_order(row[l/2+1:], key)
            else:
                return _get_order(row[:l/2], key)

        def _get_order2(row, key):
            low, high = 0, len(row)-1
            while row[low] <= key and row[high] > key:
                mid = (low + high) / 2
                if row[mid] <= key:
                    low = mid + 1
                else:
                    high = mid
            return low if row[low] > key else high + 1

        n = len(matrix)
        minv, maxv = matrix[0][0], matrix[n-1][n-1]

        while minv < maxv:
            num, mid = 0, (minv + maxv) / 2
            for row in matrix:
                num += _get_order1(row, mid)
                # num += _get_order2(row, mid)
                # num += bisect.bisect_right(row, mid)
            if num < k:
                minv = mid + 1
            else:
                maxv = mid

        return minv

s = Solution()
print s.kthSmallest([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5)
