class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """

        def parse_email_addr(email):
            local, domain = email.split('@')
            local = local.split('+')[0].replace('.', '')
            email = '@'.join([local, domain])
            return email

        return len(set([parse_email_addr(email) for email in emails]))


if __name__ == '__main__':
    input = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    assert 2 == Solution().numUniqueEmails(input), 'testcase failed'
