class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        mapping = {}
        for i, p in enumerate(pattern):
            w = f'w_{words[i]}'
            if mapping.get(w) != mapping.get(p):
                return False
            if w not in mapping:
                mapping[w] = mapping[p] = i

        return True
