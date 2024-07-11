class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        count = 0
        n = len(colors)
        for i0, color in enumerate(colors):
            i1, i2 = (i0+1) % n, (i0+2) % n
            if color == colors[i2] and color != colors[i1]:
                count += 1

        return count
