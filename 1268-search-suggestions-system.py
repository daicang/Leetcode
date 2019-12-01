class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """

        class TreeNode():
            def __init__(self, ch):
                self.ch = ch
                self.child_dict = {}
                self.suggests = []

            def has_child(self, ch):
                return ch in self.child_dict

            def get_child(self, ch):
                return self.child_dict[ch]

            def add_child(self, ch):
                child = TreeNode(ch)
                self.child_dict[ch] = child

            def add_suggest(self, word, level):
                self.suggests.append(word)
                self.suggests.sort()
                self.suggests = self.suggests[:3]

                if level < len(word)-1:
                    child = self.get_child(word[level+1])
                    child.add_suggest(word, level+1)

            def suggest(self):
                return self.suggests

        root = TreeNode('')

        # Generate prefix tree
        for prod in products:
            node = root
            for ch in prod:
                if not node.has_child(ch):
                    node.add_child(ch)
                node = node.get_child(ch)

            node = root.get_child(prod[0])
            node.add_suggest(prod, 0)

        result = []
        node = root
        miss = False
        for ch in searchWord:
            if miss:
                result.append([])
                continue

            if node.has_child(ch):
                node = node.get_child(ch)
                result.append(node.suggest())
            else:
                miss = True
                result.append([])

        return result

s = Solution()

data = [
    [["mobile","mouse","moneypot","monitor","mousepad"], "mouse"],
    [["havana"], "havana"],
    [["bags","baggage","banner","box","cloths"], "bags"],
    [["havana"], "tatiana"],
]

for i in data:
    print s.suggestedProducts(*i)


# Output: [
# ["mobile","moneypot","monitor"],
# ["mobile","moneypot","monitor"],
# ["mouse","mousepad"],
# ["mouse","mousepad"],
# ["mouse","mousepad"]
# ]
# Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
# After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
# After typing mou, mous and mouse the system suggests ["mouse","mousepad"]

# Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]

# Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]

# Output: [[],[],[],[],[],[],[]]

