#https://leetcode.com/explore/interview/card/google/59/array-and-strings/3053/


class Solution:
    def canJump(self, nums: list):
        l = len(nums)
        i,maximum = 0 , 0

        #iを一つずつ勧めていく。それがmaxと同じ値になったら終わり
        #iを１ずつすすめるのは最小の移動単位が1だから。
        #隣にうつって、となりのvalue[i] + iと、numsの長さが同じだったらtrueを返す
        #ポインタを左から動かしていって、そのvalueを足してみて配列の最後にたどり着くかを見る
        while i <= maximum :
            maximum  = max([maximum, i + nums[i]])         
            if maximum >= l - 1:
                return True
            i+=1
        
        return False

#nums = [ 2,3, 1, 1, 4 ]
nums = [ 3,2,1,0,4 ]

solution = Solution()
print(solution.canJump(nums))