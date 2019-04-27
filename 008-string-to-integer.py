class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        def isnum(ch):
            return ord('0') <= ord(ch) <= ord('9')

        str = str.strip()
        if not str:
            return 0

        start, num, flag = 0, 0, 1
        if not isnum(str[0]):
            if str[0] == '-':
                flag = -1
            elif str[0] != '+':
                return 0
            start = 1

        for ch in str[start:]:
            if not isnum(ch):
                break
            num *= 10
            num += ord(ch) - ord('0')

        if flag == 1:
            num = 2147483647 if num > 2147483647 else num
        else:
            num = -2147483648 if num > 2147483648 else num * -1
        return num

s = Solution()
print s.myAtoi('  -0012a42')
