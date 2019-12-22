class Solution(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        """
        :type s: str
        :type maxLetters: int
        :type minSize: int
        :type maxSize: int
        :rtype: int
        """
        from collections import defaultdict
        counter = defaultdict(int)
        begin = 0

        while begin < len(s):
            limit = min(len(s), begin+maxSize)
            letters = set()

            for end in range(begin, limit):
                letters.add(s[end])
                if len(letters) > maxLetters:
                    break

                if end >= begin + minSize - 1:
                    counter[s[begin:end+1]] += 1

            begin += 1

        if counter:
            return max(counter.values())
        return 0


s = Solution()

data = [
    ["aababcaab", 2, 3, 4],
    ["aaaa", 1, 3, 3],
    ["aabcabcab", 2, 2, 3],
    ["abcde", 2, 3, 3]
]

for d in data:
    print s.maxFreq(*d)

