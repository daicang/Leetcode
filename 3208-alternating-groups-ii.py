class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        count = 0
        n = len(colors)
        tail = 0
        head = 1
        while tail < n:
            while head < tail + k:
                c1, c2 = colors[head%n], colors[(head-1)%n]
                if c1 == c2:
                    tail = head
                    head = head + 1
                    break
                else:
                    head += 1
            else:
                count += 1
                tail += 1

        return count
