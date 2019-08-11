class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        l = max(len(a), len(b))

        ans = [0] * l
        flag = 0
        for i in range(1, l+1):
            if i <= len(a):
                va = int(a[-i])
            else:
                va = 0

            if i <= len(b):
                vb = int(b[-i])
            else:
                vb = 0

            # print -i, va, vb, flag
            flag, ans[-i] = divmod(va + vb + flag, 2)

        if flag:
            ans.insert(0, 1)
        return ''.join([str(i) for i in ans])


s = Solution()

print s.addBinary('1010', '1011')

