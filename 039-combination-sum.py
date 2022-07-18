class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        import copy
        candidates.sort()
        combinations = []

        def f(max_candidate_id, t, combination):

            if max_candidate_id < 0:
                return
            curr = None
            for i in range(max_candidate_id, -1, -1):
                if candidates[i] <= target:
                    curr = candidates[i]
                    break

            if curr is None:
                return

            f(i-1, t, copy.copy(combination))

            if curr == t:
                combination.append(curr)
                combinations.append(combination)
                return

            while t >= curr:
                t -= curr
                combination.append(curr)

                if t == 0:
                    combinations.append(combination)
                    break

                f(i-1, t, copy.copy(combination))

        f(len(candidates)-1, target, [])
        return combinations


s = Solution()

inputs = [
    [[2,3,6,7], 7],
    [[2,3,5], 8],
    [[2], 8],
    [[1,2], 1]
]

for input in inputs:
    print('input=%s' % input)
    print(s.combinationSum(*input))
