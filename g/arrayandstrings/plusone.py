#https://leetcode.com/explore/interview/card/google/59/array-and-strings/3054/


class Solution:
    def plusOne(self, digits: list) -> list:
        n = len(digits)
        
        for i in range(n):
            #最後の要素を見る
            idx = n - 1 - i

            # 見ている要素が9であればそこの要素を0にする
            # 0にした後次のidxにをみて繰り上がり対応をする
            if digits[idx] == 9:
                digits[idx] = 0
            else:
                # 9出ない場合はそのidxに+1をする
                digits[idx] += 1
                return digits
                
        # 全部9だったばあい、１桁追加する。
        return [1] + digits

nums = [ 1,2,3 ]

solution = Solution()
print(solution.plusOne(nums))