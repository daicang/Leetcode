class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        import copy
        from collections import Counter
        candidates.sort()
        counter = Counter(candidates)

        c = []
        last = None
        for num in candidates:
            if num == last:
                continue
            c.append(num)
            last = num

        candidates = c
        print candidates

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
                combinations.append(tuple(combination))
                return

            while counter[curr] > 0:
                t -= curr
                counter[curr] -= 1
                combination.append(curr)
                f(i-1, t, copy.copy(combination))

        f(len(candidates)-1, target, [])
        return list(set(combinations))


s = Solution()

inputs = [
    [[10,1,2,7,6,1,5], 8],
    # [[2,3,6,7], 7],
    # [[2,3,5], 8],
    # [[2], 8],
    # [[1,2], 1]
]

for input in inputs:
    print('input=%s' % input)
    print(s.combinationSum2(*input))
    print('\n')
