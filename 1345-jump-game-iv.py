
from typing import List
from collections import defaultdict, deque

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        table = defaultdict(list)
        visited = [False] * n
        visited_values = defaultdict(int)

        q = deque()
        q.append((0, 0))
        visited[0] = True

        for i in range(n):
            table[arr[i]].append(i)

        # BFS with two visited filter
        while q:
            pos, jump = q.popleft()
            if pos == len(arr)-1:
                return jump

            if pos > 0 and visited[pos-1] is False:
                visited[pos-1] = True
                q.append((pos-1, jump+1))

            if pos < len(arr)-1 and visited[pos+1] is False:
                visited[pos+1] = True
                q.append((pos+1, jump+1))

            value = arr[pos]
            if not visited_values[value]:
                visited_values[value] = True

                next_idxs = table[value]
                for next_pos in next_idxs:
                    if visited[next_pos] is False:
                        visited[next_pos] = True
                        q.append((next_pos, jump+1))

        return -1

s = Solution()

data = [
    [100,-23,-23,404,100,23,23,23,3,404],  # 3
    [7],  # 0
    [7,6,9,6,9,6,9,7],  # 1
]

for d in data:
    print(s.minJumps(d))
