class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        l = list(zip(nums2, nums1))
        l.sort(reverse=True)
        h = []
        sval = 0
        for i in range(k):
            heapq.heappush(h, l[i][1])
            sval += l[i][1]
        maxs = sval * l[k-1][0]

        for i in range(k, len(l)):
            sval -= heapq.heappop(h)
            sval += l[i][1]
            heapq.heappush(h, l[i][1])
            maxs = max(maxs, sval * l[i][0])

        return maxs