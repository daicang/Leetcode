class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0
        begin = end = 0
        while begin < n:
            end = begin
            up = down = False
            while end < n-1 and arr[end+1] > arr[end]:
                up = True
                end += 1
            while end < n-1 and arr[end+1] < arr[end]:
                down = True
                end += 1
            if up and down:
                ans = max(ans, end-begin+1)
            if end == begin:
                begin += 1
            else:
                begin = end

        return ans
