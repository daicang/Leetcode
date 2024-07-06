
from collections import defaultdict

class Solution:
    def permutation(self, s):
        n = len(s)
        results = []
        counter = defaultdict(int)
        for ch in s:
            counter[ch] += 1

        def traverse(path):
            if len(path) == n:
                results.append(''.join(path))
                return

            for ch in counter:
                if counter[ch] > 0:
                    counter[ch] -= 1
                    path.append(ch)
                    traverse(path)
                    path.pop()
                    counter[ch] += 1

        traverse([])
        return results

    def generatePalindromes(self, s: str) -> List[str]:
        counter = Counter(s)
        mid_char = ''
        chars = []
        for ch, count in counter.items():
            count2, r = divmod(count, 2)
            if r == 1:
                if mid_char:
                    # at most one odd char
                    return []
                mid_char = ch
            for _ in range(count2):
                chars.append(ch)

        palins = self.permutation(chars)
        results = []
        for palin in palins:
            results.append('%s%s%s' % (palin, mid_char, palin[::-1]))

        return results
