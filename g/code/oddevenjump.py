#During odd numbered jumps (ie. jumps 1, 3, 5, ...), you jump to the index j such that A[i] <= A[j] and A[j] is the smallest possible value.  If there are multiple such indexes j, you can only jump to the smallest such index j.
# 1,3,5の時はi>jかつA[i] <=A [j] の値のうち一番小さい値にjumpできます。
#
#During even numbered jumps (ie. jumps 2, 4, 6, ...), you jump to the index j such that A[i] >= A[j] and A[j] is the largest possible value.  If there are multiple such indexes j, you can only jump to the smallest such index j.
#2,3,6 の時は A[i] >= A[j] のうち一番大きな値にjumpできる。もし、飛び先が複数ある場合はjがもっとも小さい物にjumpする
#(It may be the case that for some index i, there are no legal jumps.)

#ここでいうodd,evenはodd 1,3,5はarrayでいう0,2,4 even 2,4,6 はarray keyでいう1,3,5になるので注意。arrayは0はじまりになるの。
#aあとでこれをやあとでこれをやる 
# https://leetcode.com/articles/sum-of-subarray-minimums/

class Solution(object):
    def oddEvenJumps(self, A):
        N = len(A)

        def make(B):
            # モノリシックスタックでarrayのうちのsubaryでmaxをstackするようにすると、次のoddjump先がわかる。
            # 引数Bの昇順お降順にすることで、逆のevenjumpの結果を求めることができる。
            # 
            ans = [None] * N
            stack = []  # invariant: stack is decreasing
            for i in B:
                print('-----')
                while stack and i > stack[-1]:
                    print(stack)
                    ans[stack.pop()] = i
                    print(ans)
                    print(stack)
                stack.append(i)
                print(stack)
                print('-----')
            return ans

        print(A)
        #lambda i: A[i] 
        # iがrangeで0-4になり、A[i]の数字でソートされて、rangeが[0, 2, 1, 3, 4]になる。
        # つまり、各要素のソートした時の順番になる。便利！！！
        B = sorted(range(N), key = lambda i: A[i])
        print(B)

        oddnext = make(B)
        B.sort(key = lambda i: -A[i])
        print(B)
        evennext = make(B)

        odd = [False] * N
        even = [False] * N
        odd[N-1] = even[N-1] = True

        test=range(N-2, -1, -1)
        print(oddnext)
        print(evennext)
        #最後の数は必ずtrueなのでそれ以外を計算している。
        #oddnext,evennextを一つずつdecreaseしながら見ていって、
        #どの一からodd evenjumpを始めると最後に到達する場所にtrueを入れていき、最後にsumをする??(ここ復讐)
        for i in range(N-2, -1, -1):
            print('i:'+str(i))
            if oddnext[i] is not None:
                odd[i] = even[oddnext[i]]
                print("odd:")
                print(odd)
                print("even:")
                print(even)
            if evennext[i] is not None:
                even[i] = odd[evennext[i]]
                print("odd:")
                print(odd)
                print("even:")
                print(even)

        return sum(odd)

solution = Solution()
#print(solution.oddEvenJumps([10,13,12,14,15]))
print(solution.oddEvenJumps([2,3,1,1,4]))