#class Solution:
#    def threeSum(self, nums: list):
#        res=[]
#        for i in range(len(nums)):
#            print(i)
#            start=i+1
#            for j in range(start, len(nums[start:])):
#                cstart=j+1
#                for c in (nums[cstart:]):
#                    print('---------------')
#                    print('a:'+ str(nums[i]))
#                    print('b:'+ str(nums[j]))
#                    print('c:'+ str(c))
#                    print('---------------')
#                    if nums[i] + nums[j] + c == 0:
#                        res.append(sorted([nums[i], nums[j], c]))
#            
#        return self.get_unique_list(res) 
#
#    def get_unique_list(self,seq):
#        seen = []
#        return [x for x in seq if x not in seen and not seen.append(x)]
#For the main function:
#
#   Sort the input array nums.
#       Iterate through the array:
#           If the current value is greater than zero, break from the loop. Remaining values cannot sum to zero.
#           ソートしてあるので、0番目からデータを見て行った時に値が0以上になった場合は成立しなくなる。合計して0なので0番目から見ていると必ずマイナス
#           If the current value is the same as the one before, skip it.
#           今見ている値と次の値が同じ場合はスキップ(結果が一緒なので) 
#           Otherwise, call twoSumII for the current position i.
#           上記でない場合にtowSumIIのメソッドを呼ぶ
# 
#       For twoSumII function:
#           Set the low pointer lo to i + 1, and high pointer hi to the last index.
#           ポインターをlo pointerをi+1にhi poriterをインデックスの最後に当てる
#           While low pointer is smaller than high:
#               If the sum of nums[i], nums[lo] and nums[hi] is less than zero, increment lo.
#               Also increment lo if the value is the same as for lo - 1.
#               loとlo-1が同じ時と、i, lo, hiの合計が0より小さいの時はloを+1する
#
#               If the sum is greater than zero, decrement hi.
#               Also decrement hi if the value is the same as for hi + 1.
#               hiの値がhi+1のものと同じ時と、3つの値の合計が0よりおおきい時はhiを-1する。
#
#               Otherwise, we found a triplet:
#               Add it to the result res.
#               Decrement hi and increment lo.
#               上記２つの条件にマッチしない場合は、求めるtripletを見つけている。
#               それをresultに追加し、hiをdecrement, loをincrementする。

class Solution:
    def threeSum(self, nums: list):
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSumII(nums, i, res)
        return res

    def twoSumII(self, nums: list, i: int, res: list):
        lo, hi = i + 1, len(nums) - 1
        while (lo < hi):
            sum = nums[i] + nums[lo] + nums[hi]
            if sum < 0 or (lo > i + 1 and nums[lo] == nums[lo - 1]):
                lo += 1
            elif sum > 0 or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1

solution = Solution()    
#print(solution.threeSum([-1, 0, 1, 2, -1, -4]))
print(solution.threeSum([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]))