class Solution:
    def doesAliceWin(self, s: str) -> bool:
        counter = Counter(s)
        count = 0
        for ch in 'aeiou':
            count += counter.get(ch, 0)
        return count > 0
