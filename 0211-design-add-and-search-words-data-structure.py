
class Node:

    def __init__(self) -> None:
        self.children = [None] * 26
        self.leaf = False

class WordDictionary:

    def __init__(self):
        self.root = Node()


    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if curr.children[idx] is None:
                curr.children[idx] = Node()
            curr = curr.children[idx]
        curr.leaf = True

    def search(self, word: str) -> bool:
        stack = [(self.root, 0)]
        while stack:
            node, idx = stack.pop()
            if idx == len(word):
                if node.leaf is True:
                    return True
                continue

            ch = word[idx]
            if ch == '.':
                for child in node.children:
                    if child:
                        stack.append((child, idx+1))
                continue

            child = node.children[ord(ch)-ord('a')]
            if child:
                stack.append((child, idx+1))

        return False


s = WordDictionary()
s.addWord('at')
s.addWord('and')
s.addWord('an')
s.addWord('add')
s.search('a')
s.search('.at')
s.addWord('bat')
s.search('.at')
s.search('an.')
s.search('a.d.')
s.search('b.')
s.search('a.d')
s.search('.')



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)