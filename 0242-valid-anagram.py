
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = {}

        for ch in s:
            if ch not in counter:
                counter[ch] = 1
            else:
                counter[ch] += 1

        for ch in t:
            if ch in counter:
                counter[ch] -= 1
                if counter[ch] == 0:
                    del counter[ch]
            else:
                return False

        return len(counter) == 0
