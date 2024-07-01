
from collections import defaultdict

class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        tree_size = [0] * n
        graph = []
        for _ in range(n):
            graph.append([])

        for child, parent in enumerate(parents):
            if child != 0:
                graph[parent].append(child)

        def get_tree_size(i):
            if tree_size[i] > 0:
                return tree_size[i]
            count = 1
            for child in graph[i]:
                count += get_tree_size(child)
            tree_size[i] = count
            return count

        get_tree_size(0)

        # score-> number of nodes
        counter = defaultdict(int)

        for i in range(n):
            value = 1
            subtree_size = 0
            for subtree in graph[i]:
                value *= tree_size[subtree]
                subtree_size += tree_size[subtree]
            if i != 0:
                parent_size = tree_size[0] - subtree_size - 1
                assert parent_size > 0
                value *= parent_size
            counter[value] += 1

        max_score = max(counter.keys())
        return counter[max_score]
