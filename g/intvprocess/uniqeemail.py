import re

class Solution:
    def numUniqueEmails(self, emails):
        res=[]
        for mail in emails:
            (name,domain) = mail.split('@')
            name = name.replace('.', '')
            name = re.sub('\+.*','', name)
            res.append(name+'@'+domain)

        return len(list(set(res)))

solution = Solution()
emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
print(solution.numUniqueEmails(emails))