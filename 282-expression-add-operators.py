class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:

        def evaluate(s):
            arr = []
            while s:
                t = s.pop()
                if isinstance(t, int):
                    if s and s[-1] == '+':
                        s.pop()
                        arr.append(t)
                    elif s and s[-1] == '-':
                        s.pop()
                        arr.append(-t)
                    elif s and s[-1] == '*':
                        s.pop()
                        t1 = s.pop()
                        assert isinstance(t1, int)
                        s.append(t * t1)
                    else:
                        assert len(s) == 0
                        arr.append(t)
            return sum(arr)

        results = []

        def bfs(i, path):
            if i == len(num):
                if evaluate(path[:]) == target:
                    path = [str(i) for i in path]
                    results.append(''.join(path))
                return

            val = int(num[i])
            if path:
                # join with last number
                prev = path.pop()
                if prev != 0:
                    path.append(prev * 10 + val)
                    bfs(i+1, path)
                    path.pop()
                    path.append(prev)
                else:
                    path.append(prev)

                # adding + - *
                for op in '+-*':
                    path.append(op)
                    path.append(val)
                    bfs(i+1, path)
                    path.pop()
                    path.pop()
            else:
                # first digit
                path.append(val)
                bfs(i+1, path)


        bfs(0, [])
        return results
