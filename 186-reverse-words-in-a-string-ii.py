from typing import List

class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(start, end):
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1

        reverse(0, len(s)-1)

        word_begin = word_end_blank = 0
        while word_begin < len(s):
            while word_end_blank < len(s) and s[word_end_blank] != ' ':
                word_end_blank += 1
            reverse(word_begin, word_end_blank-1)

            # move to start index of next word
            word_end_blank += 1
            word_begin = word_end_blank


s = Solution()

inputs = [
    ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"],
]

for i in inputs:
    s.reverseWords(i)
    print(i)
