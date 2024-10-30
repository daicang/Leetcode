class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        n = len(digits)
        arr = [0, 0,
            ('a', 'b', 'c'),
            ('d', 'e', 'f'),
            ('g', 'h', 'i'),
            ('j', 'k', 'l'),
            ('m', 'n', 'o'),
            ('p', 'q', 'r', 's'),
            ('t', 'u', 'v'),
            ('w', 'x', 'y', 'z')]

        def traverse(i, path):
            if i == n:
                if path:
                    result.append(''.join(path))
                return
            index = int(digits[i])
            for ch in arr[index]:
                path.append(ch)
                traverse(i+1, path)
                path.pop()

        traverse(0, [])
        return result
