class Solution:
    def buildMatrix(self, k: int, rows: List[List[int]], cols: List[List[int]]) -> List[List[int]]:
        # 2x topo sorting

        def build(deps, k):
            prevs = [None] * (k+1)
            nexts = [None] * (k+1)

            for i in range(1, k+1):
                prevs[i] = set()
                nexts[i] = set()

            for p, i in deps:
                prevs[i].add(p)
                nexts[p].add(i)

            order = [-1] * (k+1)
            heads = []
            cnt = 0

            for i, p in enumerate(prevs):
                if i > 0:
                    if not p:
                        heads.append(i)

            while heads:
                h = heads.pop()
                order[h] = cnt
                cnt += 1
                for n in nexts[h]:
                    prevs[n].remove(h)
                    if len(prevs[n]) == 0:
                        heads.append(n)

            for p in prevs:
                if p:
                    return []

            for i in range(1, k+1):
                if order[i] == -1:
                    order[i] = cnt
                    cnt += 1

            return order

        row_order = build(rows, k)
        col_order = build(cols, k)

        if len(row_order) == 0 or len(col_order) == 0:
            return []

        mat = []
        for _ in range(k):
            mat.append([0] * k)

        for i in range(1, k+1):
            r = row_order[i]
            c = col_order[i]
            mat[r][c] = i

        return mat