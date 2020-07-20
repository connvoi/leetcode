#https://leetcode.com/explore/interview/card/google/59/array-and-strings/3051/

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(self.atoi(num1) * self.atoi(num2))

    def atoi(self, num:str) -> int:
        inlist ={
            "0" :0,
            "1" :1,
            "2" :2,
            "3" :3,
            "4" :4,
            "5" :5,
            "6" :6,
            "7" :7,
            "8" :8,
            "9" :9
        }
        res = 0
        for i in range(len(num)):
            res = res*10 + inlist[num[i]] 




solution = Solution()