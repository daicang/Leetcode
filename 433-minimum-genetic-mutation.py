class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:

        def can_evolve(s1, s2):
            if len(s1) != len(s2):
                return False
            count = 0
            for v1, v2 in zip(s1, s2):
                if v1 != v2:
                    count += 1
                    if count > 1:
                        return False
            return True

        # number all gene series
        # start is number 0
        # bank 1 to n. find the end number

        bank = [startGene] + bank
        n = len(bank)
        endi = -1
        for i, serie in enumerate(bank):
            if serie == endGene:
                endi = i
                break
        else:
            return -1

        # create visited record

        visited = [False] * n

        # create adjacent array

        table = []
        for _ in range(n):
            table.append([0] * n)

        for i in range(n):
            for j in range(i+1):
                if i == j:
                    table[i][j] = 1
                else:
                    table[i][j] = table[j][i] = can_evolve(bank[i], bank[j])

        # deque to keep next gene to evolve
        # also keep step counter

        q = deque()
        q.append([0, 0])
        while q:
            i, step = q.popleft()
            if i == endi:
                return step
            visited[i] = True
            for j, val in enumerate(table[i]):
                if not visited[j] and val == 1:
                    q.append([j, step+1])


        # when first encounter end serie, return step
        # otherwise, return -1

        return -1
