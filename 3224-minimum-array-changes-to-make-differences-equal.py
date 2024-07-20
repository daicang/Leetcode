class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        # time: O(n^2)
        # space: O(n)
        darr = []
        dlimit = []
        n = len(nums)
        for i in range(n):
            a, b = nums[i], nums[n-i-1]
            darr.append(abs(a-b))
            dlimit.append(max(a, b, k-a, k-b))

        mincnt = n
        diffs = Counter(darr)
        darr_sorted = []
        for d, c in diffs.items():
            darr_sorted.append((c, d))
        darr_sorted.sort(reverse=True)

        for c, d in darr_sorted:
            lowerbound = n//2 - c
            if lowerbound >= mincnt:
                break

            cnt = 0
            for i in range(n//2):
                if darr[i] == d:
                    continue
                if dlimit[i] >= d:
                    cnt += 1
                else:
                    cnt += 2
                if cnt >= mincnt:
                    break

            mincnt = min(mincnt, cnt)

        return mincnt
