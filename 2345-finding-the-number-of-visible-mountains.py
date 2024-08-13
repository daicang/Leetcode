class Solution:
    def visibleMountains(self, peaks: List[List[int]]) -> int:
        n = len(peaks)
        peaks.sort(key=lambda x: (x[0]-x[1], -(x[0]+x[1])))
        count = 0
        s = -inf
        for i, (x, y) in enumerate(peaks):
            if x+y > s:
                s = x+y
                if i < n-1 and peaks[i] == peaks[i+1]:
                    continue
                count += 1

        return count
