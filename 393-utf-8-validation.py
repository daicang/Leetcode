class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        def _0byte(ch):
            return ch & 128 == 0

        def _1byte(ch):
            return ch & 224 == 192

        def _2byte(ch):
            return ch & 240 == 224

        def _3byte(ch):
            return ch & 248 == 240

        def _following_byte(ch):
            return ch & 192 == 128

        following_byte_counter = 0
        for ch in data:
            if following_byte_counter:
                following_byte_counter -= 1
                if not _following_byte(ch):
                    break
            elif _0byte(ch):
                following_byte_counter = 0
            elif _1byte(ch):
                following_byte_counter = 1
            elif _2byte(ch):
                following_byte_counter = 2
            elif _3byte(ch):
                following_byte_counter = 3
            else:
                break
        else:
            return following_byte_counter == 0
        return False

s = Solution()
print s.validUtf8([197, 130, 1])
