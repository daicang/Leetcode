class Solution:
    def kSmallestPairs(self, n1: List[int], n2: List[int], k: int) -> List[List[int]]:
        h = [(n1[0]+n2[0], 0, 0)]
        ans = []
        visited = set()

        for _ in range(k):
            s, i1, i2 = heapq.heappop(h)
            ans.append((n1[i1], n2[i2]))
            visited.add((i1, i2))
            if i1 < len(n1)-1 and (i1+1, i2) not in visited:
                visited.add((i1+1, i2))
                heapq.heappush(h, (n1[i1+1]+n2[i2], i1+1, i2))
            if i2 < len(n2)-1 and (i1, i2+1) not in visited:
                visited.add((i1, i2+1))
                heapq.heappush(h, (n1[i1]+n2[i2+1], i1, i2+1))

        return ans
