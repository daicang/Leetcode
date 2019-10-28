class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        front = 0
        end = len(s)-1

        def is_pali(s_):
            return s_ == s_[::-1]

        while front < end:
            if s[front] != s[end]:
                if is_pali(s[front+1:end+1]) or is_pali(s[front:end]):
                    return True
                else:
                    return False

            front += 1
            end -= 1

        return True

s = Solution()

inputs = [
    'aba', 'abca', 'abcca', 'abbcca'
]

for i in inputs:
    print s.validPalindrome(i)
