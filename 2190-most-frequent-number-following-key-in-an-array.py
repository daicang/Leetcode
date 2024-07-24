class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        counter = defaultdict(int)
        for i, val in enumerate(nums):
            if val == key and i < len(nums)-1:
                counter[nums[i+1]] += 1
        maxcnt = 0
        number = None
        for n, count in counter.items():
            if count > maxcnt:
                maxcnt = count
                number = n
        return number
