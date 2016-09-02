import collections


class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        recd = collections.defaultdict(lambda: 0)
        for rec in rectangles:
            lb = str(rec[:2])
            lt = str([rec[0], rec[3]])
            rb = str([rec[2], rec[1]])
            rt = str(rec[2:])

            if recd[lb] & 1:
                return False
            recd[lb] |= 1

            if recd[lt] & 2:
                return False
            recd[lt] |= 2

            if recd[rb] & 4:
                return False
            recd[rb] |= 4

            if recd[rt] & 8:
                return False
            recd[rt] |= 8

        corner = 0
        for pval in recd.itervalues():
            if pval in [1, 2, 4, 8]:
                corner += 1
            elif pval not in [3, 5, 10, 12, 15]:
                return False

        return corner == 4

s = Solution()
print s.isRectangleCover([[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]])
