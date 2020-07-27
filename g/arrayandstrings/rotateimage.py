#https://leetcode.com/explore/interview/card/google/59/array-and-strings/3052/

class Solution:
    #転置してreverseするとできる。
    #def rotate(self, matrix):
    #    n = len(matrix[0])        
    #    # transpose matrix
    #    #i = 1
    #    for i in range(n):
    #        #i = 1
    #        #j = 0,1,2 
    #        for j in range(i, n):
    #            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i] 
    #    
    #    # reverse each row
    #    for i in range(n):
    #        matrix[i].reverse()

    
    def rotate(self, matrix):
        n = len(matrix[0])
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                tmp = [0] * 4
                row, col = i, j
                # store 4 elements in tmp
                for k in range(4):
                    tmp[k] = matrix[row][col]
                    row, col = col, n - 1 - row
                # rotate 4 elements   
                for k in range(4):
                    matrix[row][col] = tmp[(k - 1) % 4]
                    row, col = col, n - 1 - row

m = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

solution = Solution()
solution.roatate(m)