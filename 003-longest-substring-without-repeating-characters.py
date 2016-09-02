#!/usr/bin/python
# longest substring without repeating characters
# not DP

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        ret = 0
        # last duplicate index
        duplicate = -1
        # index last appeared
        d = {}
        for i in range(len(s)):
            if s[i] in d:
                duplicate = max(duplicate, d[s[i]])
            ret = max(ret, i - max(d[s[i]], duplicate))
            d[s[i]] = i
        return ret
        
#         if len(s) == 0:
#             return 0
#         ret = 1
#         arr = [1]
#         for i in range(1, len(s)):
#             startidx = i - arr[i-1]
#             prevstr = s[startidx:i]
#             if prevstr.find(s[i]) == -1:
#                 arr.append(arr[i-1] + 1)
#                 if arr[i] > ret:
#                     ret = arr[i]
#             else:
#                 arr.append(1)
#         return ret

s = Solution()
print s.lengthOfLongestSubstring("")
print s.lengthOfLongestSubstring("abcabcbb")
print s.lengthOfLongestSubstring("bbbbbbb")
print s.lengthOfLongestSubstring("aab")
