class Node:
    def __init__(self):
        self.val = {}
        self.children = []
        self.term = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.val:
                node.val[ch] = Node()
            node = node.val[ch]
            node.children.append(word)
            node.children.sort()
            node.children = node.children[:3]
        node.term = True

    def find_child(self, word):
        ans = []
        node = self.root
        for i, ch in enumerate(word):
            if ch not in node.val:
                for j in range(i, len(word)):
                    ans.append([])
                break
            node = node.val[ch]
            ans.append(node.children)

        return ans


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        tree = Trie()
        for w in products:
            tree.insert(w)

        return tree.find_child(searchWord)
