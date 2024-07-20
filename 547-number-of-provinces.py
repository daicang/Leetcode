class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # Time: O(n^2)
        # Space: O(n)
        n = len(isConnected)
        visited = [False] * n
        count = 0

        for i in range(n):
            if visited[i]:
                continue
            q = [i]
            while q:
                c = q.pop()
                if visited[c]:
                    continue
                visited[c] = True
                for ni, connected in enumerate(isConnected[c]):
                    if connected and not visited[ni]:
                        q.append(ni)
            count += 1
        return count
