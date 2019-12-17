class CombinationIterator(object):

    def __init__(self, characters, combinationLength):
        """
        :type characters: str
        :type combinationLength: int
        """
        self.charset = sorted(characters)
        self.length = combinationLength

        self.it = iter(self.backtrack(0, self.length, []))
        self.ans = []

    def backtrack(self, i, left, chars):
        if left == 0:
            yield ''.join(chars)
            return
        if i >= len(self.charset):
            return

        chars.append(self.charset[i])
        for c in self.backtrack(i+1, left-1, chars):
            yield c
        chars.pop()

        for c in self.backtrack(i+1, left, chars):
            yield c

    def next(self):
        """
        :rtype: str
        """
        if self.ans:
            next_ = self.ans[0]
            self.ans = self.ans[1:]
        else:
            next_ = next(self.it)
        return next_


    def hasNext(self):
        """
        :rtype: bool
        """
        if self.ans:
            return True
        try:
            next_ = next(self.it)
        except StopIteration:
            return False
        self.ans.append(next_)
        return True

    def test(self):
        for val in self.it:
            print val


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()

s = CombinationIterator('abc', 2)

s.test()

# print s.next()
# print s.hasNext()
# print s.next()
# print s.hasNext()
# print s.next()
# print s.hasNext()
