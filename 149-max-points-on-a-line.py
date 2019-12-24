class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        from collections import Counter

        points = [(p[0], p[1]) for p in points]
        weights = Counter(points)
        points = weights.keys()

        if not points:
            return 0
        if len(points) == 1:
            return weights[points[0]]

        maxpoints = 0
        for i, p1 in enumerate(points):
            counter = {}
            for j in range(i+1, len(points)):
                p2 = points[j]
                if p1[0] == p2[0]:
                    slope = 'inf'
                else:
                    slope = (p2[1] - p1[1]) / float(p2[0] - p1[0])

                if slope not in counter:
                    counter[slope] = weights[p1] + weights[p2]
                else:
                    counter[slope] += weights[p2]

            for val in counter.values():
                maxpoints = max(maxpoints, val)

        return maxpoints


s = Solution()

data = [
    [[1,1],[2,2],[3,3]],  # 3
    [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]],  # 4
    [[0,0],[0,0]],  # 2
    [[1,1],[1,1],[2,3]],  # 3
    [[3,1],[12,3],[3,1],[-6,-1]],# 4
    [[-54,-297],[-36,-222],[3,-2],[30,53],[-5,1],[-36,-222],[0,2],[1,3],[6,-47],[0,4],[2,3],[5,0],[48,128],[24,28],[0,-5],[48,128],[-12,-122],[-54,-297],[-42,-247],[-5,0],[2,4],[0,0],[54,153],[-30,-197],[4,5],[4,3],[-42,-247],[6,-47],[-60,-322],[-4,-2],[-18,-147],[6,-47],[60,178],[30,53],[-5,3],[-42,-247],[2,-2],[12,-22],[24,28],[0,-72],[3,-4],[-60,-322],[48,128],[0,-72],[-5,3],[5,5],[-24,-172],[-48,-272],[36,78],[-3,3]],  # 30
    [[84,250],[0,0],[1,0],[0,-70],[0,-70],[1,-1],[21,10],[42,90],[-42,-230]],     # 6
]

for d in data:
    print s.maxPoints(d)

