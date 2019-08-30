class Solution(object):
    def isInterleave_backtrack(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        # TLE
        if len(s3) != len(s1) + len(s2):
            return False

        def backtrack(i1, i2, i3):
            if i3 == len(s3):
                return True
            if i1 == len(s1):
                return s2[i2:] == s3[i3:]
            if i2 == len(s2):
                return s1[i1:] == s3[i3:]

            if s3[i3] == s1[i1]:
                if backtrack(i1+1, i2, i3+1):
                    return True

            if s3[i3] == s2[i2]:
                if backtrack(i1, i2+1, i3+1):
                    return True

            return False

        return backtrack(0, 0, 0)

    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s3) != len(s1) + len(s2):
            return False

        cache = []
        for _ in range(len(s1)+1):
            cache.append([None] * (len(s2)+1))

        def backtrack(i1, i2, i3):
            if cache[i1][i2] is not None:
                return cache[i1][i2]

            if i3 == len(s3):
                cache[i1][i2] = True
                return True

            if i1 == len(s1):
                val = s2[i2:] == s3[i3:]
                cache[i1][i2] = val
                return val

            if i2 == len(s2):
                val = s1[i1:] == s3[i3:]
                cache[i1][i2] = val
                return val

            if s3[i3] == s1[i1]:
                if backtrack(i1+1, i2, i3+1):
                    cache[i1][i2] = True
                    return True

            if s3[i3] == s2[i2]:
                if backtrack(i1, i2+1, i3+1):
                    cache[i1][i2] = True
                    return True

            cache[i1][i2] = False
            return False

        return backtrack(0, 0, 0)




s = Solution()


inputs = [
    ["aabcc", "dbbca", "aadbbcbcac"],  # true
    [ "aabcc", "dbbca", "aadbbbaccc"]  # false
]

for i in inputs:
    print s.isInterleave(*i)

