# 331-verify-preorder-serialization-of-binary-tree.py

class Solution(object):
    def isValidSerialization_TLE(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        def loop(l):
            length = len(l)
            if length < 3:
                if length == 1 and l[0] == '#': return True
                return False
            if l[0] == '#': return False

            for i in xrange(2, length):
                if loop(l[1:i]) and loop(l[i:]): return True
            return False

        l = preorder.split(',')
        return loop(l)

    def isValidSerialization(self, preorder):
        diff = 1 # In order - out order
        for i in preorder.split(","):
            diff -= 1
            if diff < 0: return False
            if i != '#':
                diff += 2
                
        return True if diff == 0 else False

s = Solution()
print(s.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"))
print(s.isValidSerialization("9,9,9,9,9,#,#,#,9,#,9,9,#,#,#,9,9,9,9,9,#,#,9,#,9,9,#,#,#,9,9,#,#,#,9,#,#,9,9,9,#,#,#,9,#,#,9,9,9,#,#,#,9,9,9,9,#,9,#,9,#,#,9,#,#,9,#,#,9,#,#"))
