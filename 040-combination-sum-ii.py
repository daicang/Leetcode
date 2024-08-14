class Solution:
    def combinationSum2(self, arr: List[int], target: int) -> List[List[int]]:
        # dfs backtrack
        arr.sort()
        results = []
        n = len(arr)

        def traverse(i, target, path):
            if target == 0:
                results.append(path[:])
            for j in range(i, n):
                if arr[j] > target:
                    break
                if j > i and arr[j] == arr[j-1]:
                    continue
                path.append(arr[j])
                traverse(j+1, target-arr[j], path)
                path.pop()

        traverse(0, target, [])
        return results
