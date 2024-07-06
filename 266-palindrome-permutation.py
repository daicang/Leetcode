
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = Counter(s)
        has_mid = False
        for val in counter.values():
            if val % 2 == 1:
                if has_mid:
                    return False
                has_mid = True
        return True
