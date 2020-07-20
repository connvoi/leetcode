#https://leetcode.com/articles/next-permutation/

class Solution:
    def nextPermutation(self, nums: list) -> None:
        '''
        find first decrease element
        配列の最後から１つずつiが下がっていく
        iの要素 > iの次の要素 が成立する場所を探す
        '''
        i = len(nums) - 2
        while(i >=0 and nums[i+1] <= nums[i]):
            i-=1
        
        '''
        jを使い、iより大きい場所で、iの要素より大きい要素(nums[i]<nums[j]を探していき、存在する場合iとjをスワップする
        swapした後、i番目から最後までをreverse（反転する)する。そうするとnext permutationが出てくる。
        
        '''
        if i >= 0:
            j = len(nums) - 1
            while(j>=0 and nums[j] <= nums[i]):
                j-=1
            nums=self.swap(nums, i, j)
        self.reverse(nums, i+1)


    def reverse(self, nums: list, start: int) :
        i = start
        j = len(nums) - 1

        while (i < j) :
            nums=self.swap(nums, i, j)
            i+=1
            j-=1


    def swap(self, nums: list, i: int, j:int):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        return nums


solution = Solution()
print(solution.nextPermutation([1,2,3]))