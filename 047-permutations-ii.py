
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counter = defaultdict(int)
        results = []

        for n in nums:
            counter[n] += 1

        def traverse(path):
            # dfs traverse with dict for de-duplication
            if len(path) == len(nums):
                results.append(path[:])
                return

            for n, count in counter.items():
                if count > 0:
                    counter[n] -= 1
                    path.append(n)
                    traverse(path)
                    path.pop()
                    counter[n] += 1

        traverse([])
        return results
