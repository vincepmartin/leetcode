class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """

        emailDict = {}
        totalMails = 0

        for email in emails:
            eTemp = self.parseEmail(email)
            if eTemp in emailDict:
                emailDict[eTemp] = True
            else:
                emailDict[eTemp] = True
                totalMails += 1

        return totalMails

    # Parse an email and get shanangans.    
    def parseEmail(self, email):
        """
        :type email: String
        :rtype: String
        """ 
        temp = email.split("@")
        email = [] 

        for c in temp[0]:
            if c == "+":
                break

            if c != ".":
                email.append(c)

        return ''.join(email) + "@" + temp[1]

         
s = Solution()
t = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
print(s.numUniqueEmails(t))
            