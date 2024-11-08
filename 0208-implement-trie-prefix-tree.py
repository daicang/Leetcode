
class Node:
    def __init__(self):
        self.val = {}
        self.end = False

class Trie:

    def __init__(self):
        self.root = Node()


    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.val:
                node.val[ch] = Node()
            node = node.val[ch]
        node.end = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.val:
                return False
            node = node.val[ch]
        return node.end


    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node.val:
                return False
            node = node.val[ch]
        return True
