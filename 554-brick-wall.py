class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        n = sum(wall[0])
        # (0 .. n), open interval
        counter = defaultdict(int)
        l = len(wall)

        for layer in wall:
            i = 0
            for w in layer:
                i += w
                if i < n:
                    counter[i] += 1
        if not counter:
            return l
        return l - max(counter.values())
