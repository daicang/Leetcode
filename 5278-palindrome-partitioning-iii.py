class Solution(object):
    def palindromePartition(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        palin_price = []
        for _ in s:
            # palin_price[begin][end]: Number of characters to change s[begin:end+1] to palindrome
            palin_price.append([None] * len(s))

        results = []
        # results[begin][end][partition]
        for i1 in range(len(s)):
            results.append([])
            for _ in s:
                results[i1].append([None] * (k+1))

        def get_price(begin, end):
            # [begin, end], inclusive
            if end <= begin:
                return 0

            cached = palin_price[begin][end]
            if cached:
                return cached

            price = get_price(begin+1, end-1)
            if s[begin] != s[end]:
                price += 1
            palin_price[begin][end] = price
            return price

        def solve(begin, end, partition):
            # [begin, end], inclusive
            if results[begin][end][partition] is not None:
                return results[begin][end][partition]

            if partition == 1:
                return get_price(begin, end)

            if begin == end:
                return 0

            min_price = None
            for split_idx in range(begin+1, end+1):
                # [begin, split_idx) [split_idx, end]
                price_ = get_price(begin, split_idx-1) + solve(split_idx, end, partition-1)
                if min_price is None:
                    min_price = price_
                else:
                    min_price = min(min_price, price_)

            results[begin][end][partition] = min_price
            return min_price

        return solve(0, len(s)-1, k)


s = Solution()

data = [
    ['abc', 2],  # 1
    ['aabbc', 3],  # 0
    ['leetcode', 8],  # 0
    ["mdgvmhrxusevwnneyzkfaqpceoof", 9],  # 8
    ["ihhyviwv", 7]
]

for d in data:
    print s.palindromePartition(*d)
