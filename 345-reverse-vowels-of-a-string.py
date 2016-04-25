# 345-reverse-vowels-of-a-string.py

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        def isVowel(c):
            return c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u' or c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U'

        i = 0
        j = len(s) - 1
        l = [x for x in s]

        while i < j:
            while not isVowel(s[i]) and i < j: i += 1
            while not isVowel(s[j]) and i < j: j -= 1
            if i >= j: break
            l[i], l[j] = s[j], s[i]
            i += 1
            j -= 1

        return ''.join(l)

s = Solution()
print(s.reverseVowels("hello"))
