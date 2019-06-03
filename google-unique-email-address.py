class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        count = 0

        unique_emails = set()
        for addr in emails:
            cleaned_addr = ''
            name, site = addr.split('@')
            for char in name:
                if char == '.':
                    continue
                if char == '+':
                    break
                cleaned_addr += char
            cleaned_addr += '@%s' % site
            unique_emails.add(cleaned_addr)
        return len(unique_emails)

