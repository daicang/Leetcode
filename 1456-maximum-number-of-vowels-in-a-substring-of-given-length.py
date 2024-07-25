class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        max_count = 0
        vowels = 'aeiou'

        begin = 0
        for end, ch in enumerate(s):
            if ch in vowels:
                count += 1
            while end - begin + 1 > k:
                if s[begin] in vowels:
                    count -= 1
                begin += 1
            max_count = max(max_count, count)

        return max_count
