class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        arr1 = [0] * 26

        def toint(ch):
            return ord(ch)-ord('a')

        def toch(i):
            return chr(ord('a')+i)

        first = True
        for s in A:
            arr2 = [0] * 26
            if first:
                for ch in s:
                    arr1[toint(ch)] += 1
                first = False
            else:
                for ch in s:
                    arr2[toint(ch)] += 1
                for idx, val in enumerate(arr2):
                    arr1[idx] = min(arr1[idx], val)

        ans = []
        print(arr1)
        for idx, val in enumerate(arr1):
            for _ in range(val):
                ans.append(toch(idx))
        return ans

s = Solution()
print(s.commonChars(["bella","label","roller"]))
