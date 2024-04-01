class Solution:
    def reverseWords(self, s: str) -> str:
        rs = s[::-1]
        words = rs.split()
        new_words = [w[::-1] for w in words]
        return ' '.join(new_words)