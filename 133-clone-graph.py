# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

class Solution(object):
    def __init__(self):
        self.node_map = {}

    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node.val in self.node_map:
            return self.node_map[node.val]

        node_copy = Node(node.val, [])
        self.node_map[node.val] = node_copy

        for neighbor in node.neighbors:
            node_copy.neighbors.append(self.cloneGraph(neighbor))

        return node_copy

