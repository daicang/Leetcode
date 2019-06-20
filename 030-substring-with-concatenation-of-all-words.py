class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        indexes = []
        if len(words) == 0:
            return []

        wlen = len(words[0])
        wlen_total = wlen * len(words)

        if len(s) < wlen_total:
            return []

        import copy
        from collections import defaultdict
        wd = defaultdict(int)
        for word in words:
            wd[word] += 1

        for i in range(len(s) - wlen_total + 1):
            substr = s[i:i+wlen_total]
            # print substr

            j = 0
            counter = copy.copy(wd)
            match = True

            for _ in range(len(words)):
                curr = substr[j:j+wlen]
                j += wlen
                # print curr

                if curr not in counter or counter[curr] == 0:
                    match = False
                    # print counter
                    break

                counter[curr] -= 1

            for val in counter.values():
                if val != 0:
                    match = False
                    break

            if match:
                indexes.append(i)

        return indexes

s = Solution()

inputs = [
    ("barfoothefoobarman", ["foo","bar"]),
    ("", []),
    ("wordgoodgoodgoodbestword", ["word","good","best","good"]),
]

for input in inputs:
    print s.findSubstring(*input)
