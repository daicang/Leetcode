class Solution(object):
    def minFallingPathSum(self, arr):
        """
        :type arr: List[List[int]]
        :rtype: int
        """
        if not arr or not arr[0]:
            return 0

        cache = []
        c_length = len(arr[0])
        for _ in arr:
            cache.append([None] * c_length)

        def dp(rid, disabled_cid):
            if rid >= len(arr):
                return 0

            if cache[rid][disabled_cid] is not None:
                return cache[rid][disabled_cid]

            min_idx = None
            min_path = None
            for cid in range(c_length):
                if cid == disabled_cid:
                    continue

                cost = arr[rid][cid] + dp(rid+1, cid)
                if min_path is None or cost < min_path:
                    min_path = cost
                    min_idx = cid

            cache[rid][disabled_cid] = min_path

            cost = arr[rid][disabled_cid] + dp(rid+1, disabled_cid)
            if cost < min_path:
                min_path = cost
                min_idx = disabled_cid

            for cid in range(c_length):
                if cid != min_idx:
                    cache[rid][cid] = min_path

            return cache[rid][disabled_cid]

        return dp(0, -1)


s = Solution()

data = [
    [[1,2,3],[4,5,6],[7,8,9]],  # 13
    [[-73,61,43,-48,-36],[3,30,27,57,10],[96,-76,84,59,-15],[5,-49,76,31,-7],[97,91,61,-46,67]],  # -192
]

for d in data:
    print s.minFallingPathSum(d)

