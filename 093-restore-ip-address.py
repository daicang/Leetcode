class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []

        def solve(i, l):
            if i == len(s):
                if len(l) == 4:
                    result.append('.'.join(l))
                return

            if len(l) == 4:
                return

            l.append(s[i])
            solve(i+1, l)
            l.pop()

            if s[i] != '0':
                if i+2 <= len(s):
                    l.append(s[i:i+2])
                    solve(i+2, l)
                    l.pop()

                if i+3 <= len(s) and int(s[i:i+3]) < 256:
                    l.append(s[i:i+3])
                    solve(i+3, l)
                    l.pop()

        solve(0, [])
        return result


s = Solution()
print s.restoreIpAddresses("25525511135")
