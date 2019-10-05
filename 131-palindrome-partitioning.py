class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        import copy

        def is_palindrome(s):
            for i in range(len(s)/2):
                if s[i] != s[-i-1]:
                    return False
            return True

        dp_cache = [None] * (len(s)+1)

        def solve(start_index):
            if dp_cache[start_index] is not None:
                return dp_cache[start_index]

            if start_index == len(s)-1:
                return [[s[-1]]]

            if start_index == len(s):
                return [[]]

            result = []
            for end_index in range(start_index+1, len(s)+1):
                front = s[start_index:end_index]
                if is_palindrome(front):
                    for part in copy.deepcopy(solve(end_index)):
                        part.insert(0, front)
                        result.append(part)

            # print result
            dp_cache[start_index] = result
            return result

        return solve(0)

    def dfs_partition(self, s):

        def is_pali(s):
            return s == s[::-1]

        def dfs(s, path, res):
            if not s:
                res.append(path)
                return

            for i in range(1, len(s)+1):
                if is_pali(s[:i]):
                    dfs(s[i:], path+[s[:i]], res)

        res = []
        dfs(s, [], res)
        return res



s = Solution()

inputs = [
    # 'ab',
    # 'aab',
    # 'bb',
    "abbab",
]

for i in inputs:
    print s.partition(i)

