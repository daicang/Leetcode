from collections import Counter

class Solution:
    def removeDuplicateLetters_0(self, s: str) -> str:
        if not s:
            return s

        count = Counter(s)
        pos = 0

        for i, ch in enumerate(s):
            count[ch] -= 1
            if ch < s[pos]:
                pos = i
            if count[ch] == 0:
                break

        ch = s[pos]
        s_next = s[pos+1:]
        s_next = s_next.replace(ch, '')

        return ch + self.removeDuplicateLetters(s_next)

    def removeDuplicateLetters(self, s):
        if not s:
            return s

        count = Counter(s)
        used = [False] * len(s)

        # For ch, find if there is a smaller ch in the rest of the string
        for i, ch in enumerate(s):
            count[ch] -= 1
            if count[ch] == 0:
                # ch is the last one, take it
                used[i] = True
            else:
                # ch can be postponed
                j = i+1
                used[i] = True
                while j < len(s):
                    if s[j] < ch:
                        used[i] = False
                        break
                    j += 1

        return ''.join([s[i] for i, inuse in enumerate(used) if inuse])


s = Solution()

inputs = [
    "bcabc", # abc
    "cbacdcbc" # acdb
]

for i in inputs:
    print(s.removeDuplicateLetters(i))
