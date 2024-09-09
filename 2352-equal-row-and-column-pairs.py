
class Node:
    def __init__(self):
        self.count = 0
        self.children = {}

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, row):
        node = self.root
        for ch in row:
            if ch not in node.children:
                node.children[ch] = Node()
            node = node.children[ch]
        node.count += 1

    def search(self, row):
        node = self.root
        for ch in row:
            if ch not in node.children:
                return 0
            node = node.children[ch]
        return node.count


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        trie = Trie()
        pairs = 0
        for row in grid:
            trie.insert(row)
        rows, cols = len(grid), len(grid[0])
        for c in range(cols):
            col = [grid[r][c] for r in range(rows)]
            pairs += trie.search(col)
        return pairs
