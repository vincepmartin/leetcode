from typing import List
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        mailCount = set()

        for email in emails:
            first, domain = email.split('@')
            # Process both . and +
            # . gets removed.
            # + means everything after + is ignored.
            newMail = first.replace('.', '').split('+')[0] + '@' + domain
            mailCount.add(newMail)
            print(f'{email} vs {newMail}')
        return len(mailCount)

s = Solution()
t1 = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
t2 = ["test.email+alex@leetcode.com","test.email.leet+alex@code.com"]
print(s.numUniqueEmails(t2))
       