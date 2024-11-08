class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        back = 0
        start = 0
        results = []

        for front, n in enumerate(nums):
            # slide window
            if front-back+1 > k:
                back += 1
                start = max(start, back)

            # update start
            if n != nums[front-1]+1:
                start = front

            # push results
            if front-back+1 == k:
                if start == back:
                    results.append(n)
                else:
                    results.append(-1)

        return results
