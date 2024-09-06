class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # Sliding window
        # Time: O(nlogn)
        # Space: O(n)
        fi, bi = 0, 0
        maxlen = 0
        maxh = []
        minh = []
        for fi, val in enumerate(nums):
            heapq.heappush(maxh, (-val, fi))
            heapq.heappush(minh, (val, fi))
            while -(maxh[0][0]) - minh[0][0] > limit:
                # move back pointer
                bi = min(maxh[0][1], minh[0][1]) + 1
                while maxh[0][1] < bi:
                    heapq.heappop(maxh)
                while minh[0][1] < bi:
                    heapq.heappop(minh)
            maxlen = max(maxlen, fi-bi+1)
        return maxlen

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # Time: O(nlogn)
        # Space: O(n)
        window = SortedDict()
        li = 0
        maxlen = 0

        for ri, val in enumerate(nums):
            if val in window:
                window[val] += 1
            else:
                window[val] = 1

            while window.peekitem(-1)[0] - window.peekitem(0)[0] > limit:
                window[nums[li]] -= 1
                if window[nums[li]] == 0:
                    window.pop(nums[li])
                li += 1
            maxlen = max(maxlen, ri-li+1)
        return maxlen

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # Double monotonic queue
        # Time: O(n)
        # Space: O(n)
        maxq = deque()  # max elements from li to ri
        minq = deque()  # min elements from li to ri
        li = 0
        maxlen = 0

        for ri, val in enumerate(nums):
            while maxq and maxq[-1] < val:
                maxq.pop()
            maxq.append(val)

            while minq and minq[-1] > val:
                minq.pop()
            minq.append(val)

            while maxq[0] - minq[0] > limit:
                if maxq[0] == nums[li]:
                    maxq.popleft()
                if minq[0] == nums[li]:
                    minq.popleft()
                li += 1

            maxlen = max(maxlen, ri-li+1)

        return maxlen