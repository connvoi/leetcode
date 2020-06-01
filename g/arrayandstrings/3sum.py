class Solution:
    def threeSum(self, nums: list):
        res=[]
        for i in range(len(nums)):
            print(i)
            start=i+1
            for j in range(start, len(nums[start:])):
                cstart=j+1
                for c in (nums[cstart:]):
                    print('---------------')
                    print('a:'+ str(nums[i]))
                    print('b:'+ str(nums[j]))
                    print('c:'+ str(c))
                    print('---------------')
                    if nums[i] + nums[j] + c == 0:
                        res.append(sorted([nums[i], nums[j], c]))
            
        return self.get_unique_list(res) 

    def get_unique_list(self,seq):
        seen = []
        return [x for x in seq if x not in seen and not seen.append(x)]

solution = Solution()    
#print(solution.threeSum([-1, 0, 1, 2, -1, -4]))
print(solution.threeSum([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]))