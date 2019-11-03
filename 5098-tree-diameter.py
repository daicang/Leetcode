class Solution(object):
    def treeDiameter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        # node -> {child-nodes}
        children = {}

        for parent, child in edges:
            if parent not in children:
                children[parent] = set([child])
            else:
                children[parent].add(child)

        max_path_len = [0]
        assert 0 in children, 'Root node 0 has no child'
        import heapq
        root = 0

        def calc_node(node):
            if node not in children:
                # no child node
                return 0

            child_lens = []
            for child in children[node]:
                heapq.heappush(child_lens, calc_node(child)+1)

            if len(child_lens) == 1:
                max_child_1, max_child_2 = child_lens[0], 0
            else:
                max_child_1, max_child_2 = heapq.nlargest(2, child_lens)

            # print node, max_child_1, max_child_2
            max_path_len[0] = max(max_path_len[0], max_child_1+max_child_2)

            return max_child_1

        calc_node(root)

        return max_path_len[0]


s = Solution()

inputs = [
    [[0,1],[1,2],[2,3],[1,4],[4,5]],  # 4
    [[0,1],[0,2]],
    [[0,1],[0,2],[1,3],[0,4],[1,5],[2,6],[1,7]], # 4
]

for i in inputs:
    print s.treeDiameter(i)
