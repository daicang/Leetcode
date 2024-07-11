class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        prefix_counts = defaultdict(int)
        count = 0

        for n in nums:
            curr_counts = defaultdict(int)
            curr_counts[n] += 1

            for val, c in prefix_counts.items():
                curr_counts[val & n] += c

            count += curr_counts[k]
            prefix_counts = curr_counts

        return count
