class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        desc = '1'
        if n == 1:
            return desc

        for i in range(2, n+1):
            last_ch = None
            counter = 0

            last_desc = desc
            desc = ''

            for idx, ch in enumerate(last_desc):
                if ch == last_ch:
                    counter += 1

                if idx == 0:
                    last_ch = ch
                    counter = 1

                if ch != last_ch:
                    assert counter > 0
                    desc += '%s%s' % (counter, last_ch)
                    counter = 1
                    last_ch = ch

            desc += '%s%s' % (counter, last_ch)

        return desc



