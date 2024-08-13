class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        self.count = 0
        self.graph = defaultdict(list)

        for src, dst in edges:
            self.graph[src].append(dst)
            self.graph[dst].append(src)

        def traverse(i, parent):
            size = 1
            csize = None
            for child in self.graph[i]:
                if child == parent:
                    continue
                child_size = traverse(child, i)
                size += child_size
                if csize is None:
                    csize = child_size
                else:
                    if child_size != csize:
                        csize = -1
            if csize != -1:
                self.count += 1

            return size

        traverse(0, 0)
        return self.count