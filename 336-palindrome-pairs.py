# 336-palindrome-pairs.py

class Solution(object):
    """
    :type words: List[str]
    :rtype: List[List[int]]
    """
    # Brute force
    # def palindromePairs(self, words):
    #     def isPalindrome(w):
    #         return w == w[::-1]
    #     ret = []
    #     for i in range(len(words)):
    #         for j in range(len(words)):
    #             if i == j: continue
    #             if (isPalindrome(words[i]+words[j])): ret.append([i, j])
    #     return ret

    def palindromePairs(self, words):
        def isPalindrome(w):
            return w == w[::-1]

        ret = []
        l = len(words)
        rdict = {} # reversed dict

        for i in xrange(l):
            # if words[i] == "":
            #     for j in xrange(l):
            #         if i == j: continue
            #         if isPalindrome(words[j]):
            #             ret.append([i, j])
            #             ret.append([j, i])
            #     continue
            rdict[words[i][::-1]] = i
        
        for i in xrange(l):
            curr = words[i]
            if curr != "" and isPalindrome(curr) and "" in rdict:
                ret.append([rdict[""], i])
            for j in xrange(len(curr)):
                left = curr[:j] # could be ""
                right = curr[j:] # "" not included
                if left in rdict and isPalindrome(right) and rdict[left] != i:
                    ret.append([i, rdict[left]])
                if right in rdict and isPalindrome(left) and rdict[right] != i:
                    ret.append([rdict[right], i])
                
        return ret

s = Solution()
print(s.palindromePairs(["abcd","dcba","lls","s","sssll"]))
