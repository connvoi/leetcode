#In a row of trees, the i-th tree produces fruit with type tree[i].
#
#You start at any tree of your choice, then repeatedly perform the following steps:
#
#Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
#Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.
#Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.
#
#You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.
#What is the total amount of fruit you can collect with this procedure?

#2つのバスケットを持っていて、バスケットは１種類の果物しか入らない。ただし同じ種類であれば何個でも入る。
#複数の果物の種類の木が並んでいて(treeという配列)、木から果物を撮った場合、右の木に動き、果物をとる。右に動いていき、木がなくなるか、バスケットに入らなくなる(3種類目を取得しようとする)と終了
#以上の条件の元、取得できるフルーツの最大の値をもとめよ。
#

class Solution(object):
    def totalFruit(self, tree):
        last_fruit = -1
        second_last_fruit = -1
        last_fruit_count =0
        current_max =0
        result_max = 0

        for fruit in tree:
            if fruit == last_fruit or fruit == second_last_fruit:
                current_max += 1
            else:
                current_max = last_fruit_count + 1
            
            if fruit == last_fruit :
                last_fruit_count += 1
            else:
                last_fruit_count =1

            if fruit != last_fruit:
                second_last_fruit =last_fruit
                last_fruit = fruit
        
            result_max = max(current_max, result_max)
            print('-----')
            print('fruit:'+ str(fruit))
            print('last_fruit:'+ str(last_fruit))
            print('second_last_fruit:'+ str(second_last_fruit))
            print('last_fruit_count:'+ str(last_fruit_count))
            print('now_max:'+ str(now_max))
            print('current_max:'+ str(current_max))
            print('-----')

        return result_max

solution = Solution()
print(solution.totalFruit([1,2,1]))
print(solution.totalFruit([1, 1, 1, 1, 2, 2, 3, 3, 3]))