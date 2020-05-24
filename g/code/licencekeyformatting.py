#You are given a license key represented as a string S which consists only alphanumeric character and dashes. The string is separated into N+1 groups by N dashes.
#
#Given a number K, we would want to reformat the strings such that each group contains exactly K characters, except for the first group which could be shorter than K, but still must contain at least one character. 
# Furthermore, there must be a dash inserted between two groups and all lowercase letters should be converted to uppercase.
#
#Given a non-empty string S and a number K, format the string according to the rules described above.

#半角英数で当られたlicence keyをSとする。SはN個のdash(-)でN+1のグールプに分けることができる
#数字Kが与えられて、全てのグループをK文字で構成されるグループにreformatしたい。一番初めのグループのみK以下の文字でかつ一文字以上になって良い。また、２つのグループの間には必ずdash(-)が入り、小文字は大文字になる。
#上記のルールでS,Kは与えられ、SとKは空ではない。

"""
Input: S = "5F3Z-2e-9-w", K = 4

Output: "5F3Z-2E9W"

Explanation: The string S has been split into two parts, each part has 4 characters.
Note that the two extra dashes are not needed and can be removed.
"""

class Solution(object):
    def licenseKeyFormatting(self, S , K):
        S=S.replace('-','')
        t=''
        r=[]
        for i in range(len(S)-1,-1,-1):
            t=t+S[i]
            if len(t) == K:
                r.append(''.join(reversed(t.upper())))
                t=''
        
        if len(t) > 0:
            r.append(''.join(reversed(t.upper())))
        
        return "-".join(r[::-1])

class Solution_2nd(object):
    def licenseKeyFormatting(self, S , K):
        result=[]
        #revercedされて逆順にSを呼び出す。
        for i in reversed(range(len(S))):
            if S[i] == '-':
                continue
            #K+1にして、K+1で割ったあまりがKの時が文字の切れ目になる。
            #dashを考慮するため+1する必要がある。
            #例 K=4の時 4 % 5 = 0...4となる。
            if len(result) % (K + 1) == K:
                print(len(result))
                print(len(result) % (K + 1))
                print("----")
                result += '-'
            result += S[i].upper()
        return "".join(result[::-1])

solution = Solution()
solution2 = Solution_2nd()
#print(solution.licenseKeyFormatting("5F3Z-2e-9-w",4))
#print(solution.licenseKeyFormatting("2-5g-3-J",2))
print(solution2.licenseKeyFormatting("2-4A0r7-4ki-222333-5555555",4))