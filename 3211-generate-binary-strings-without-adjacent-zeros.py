class Solution:
    def validStrings(self, n: int) -> List[str]:
        results = []

        def traverse(path, n):
            if n == 0:
                results.append(''.join(path))
                return

            if len(path) == 0 or path[-1] == '1':
                for ch in ('0', '1'):
                    path.append(ch)
                    traverse(path, n-1)
                    path.pop()
            else:
                path.append('1')
                traverse(path, n-1)
                path.pop()

        traverse([], n)
        return results
