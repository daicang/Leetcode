class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        from collections import defaultdict
        longest = 0
        counter = defaultdict(int)

        i1 = i2 = 0
        while i2 < len(s):
            counter[s[i2]] += 1
            if len(counter) <= 2:
                longest = max(longest, i2-i1+1)
            else:
                while len(counter) > 2:
                    counter[s[i1]] -= 1
                    if counter[s[i1]] == 0:
                        del counter[s[i1]]
                    i1 += 1
            i2 += 1

        return longest

s = Solution()

data = [
    "eceba",
    "ccaabbb",
    'a'
]

for d in data:
    print(s.lengthOfLongestSubstringTwoDistinct(d))
