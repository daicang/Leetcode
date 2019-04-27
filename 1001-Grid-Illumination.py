class Solution(object):
    def gridIllumination(self, N, lamps, queries):
        """
        :type N: int
        :type lamps: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """

        from collections import defaultdict

        x_dict = defaultdict(list)
        y_dict = defaultdict(list)
        x_plus_y = defaultdict(list)
        x_minus_y = defaultdict(list)

        for idx, coordinate in enumerate(lamps):
            x, y = coordinate
            x_dict[x].append(idx)
            y_dict[y].append(idx)
            x_plus_y[x+y].append(idx)
            x_minus_y[x-y].append(idx)

        ans = []
        for qx, qy in queries:
            # print x_dict, y_dict, x_plus_y, x_minus_y

            if x_dict[qx] or y_dict[qy]:
                ans.append(1)
            elif x_plus_y[qx+qy] or x_minus_y[qx-qy]:
                ans.append(1)
            else:
                ans.append(0)

            for x in range(qx-1, qx+2):
                for idx in x_dict[x]:
                    y = lamps[idx][1]
                    if y in (qy-1, qy, qy+1):
                        # print('removing %s,%s' % (x, y))
                        # remove lamp[idx]
                        x_dict[x].remove(idx)
                        y_dict[y].remove(idx)
                        x_plus_y[x+y].remove(idx)
                        x_minus_y[x-y].remove(idx)

        return ans


s = Solution()

inputs = [
    [5, [[0,0], [1,0]], [[1,1], [1,1]]],  # [1,0]
    [5, [[0,0],[0,1],[0,4]], [[0,0],[0,1],[0,2]]],  # [1,1,1]
    [5, [[0,0], [4,4]], [[1,1], [1,1]]], # [1,1]
]

for arg in inputs:
    print(s.gridIllumination(*arg))
    print('')