class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """

        lines = []

        def concate_line(words, is_last=False):
            if is_last:
                line = ' '.join(words)
                spaces = maxWidth - len(line)
                line += ' ' * spaces
                lines.append(line)
            else:
                word_width = sum([len(w) for w in words])
                spaces = maxWidth - word_width
                if len(words) > 1:
                    avg_space = spaces / (len(words)-1)
                    remainder_space = spaces - avg_space * (len(words)-1)
                else:
                    avg_space = spaces
                    remainder_space = 0

                line = ''
                for idx, w in enumerate(words):
                    line += w
                    line += ' ' * avg_space
                    if idx < remainder_space:
                        line += ' '
                if len(words) > 1:
                    line = line.strip()
                lines.append(line)

        line = []
        width = 0

        for i, word in enumerate(words):
            if width+len(word) > maxWidth:
                concate_line(line, is_last=False)
                line = []
                width = 0

            if i == len(words) - 1:
                line.append(word)
                concate_line(line, is_last=True)
                break

            line.append(word)
            width += len(word) + 1  # insert a space

        return lines


s = Solution()
inputs = [
    [["This", "is", "an", "example", "of", "text", "justification."], 16],
    [["What","must","be","acknowledgment","shall","be"], 16],
    [["Science","is","what","we","understand","well","enough","to","explain", "to","a","computer.","Art","is","everything","else","we","do"], 20]
]

for i in inputs:
    s.fullJustify(*i)
    print '\n'
