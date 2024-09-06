class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n
        q = deque([0])

        while q:
            rm = q.popleft()
            if visited[rm]:
                continue
            visited[rm] = True
            for key in rooms[rm]:
                if not visited[key]:
                    q.append(key)

        for v in visited:
            if not v:
                return False
        return True
