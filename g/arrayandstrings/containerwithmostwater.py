
#class Solution:
#    def maxArea(self, height: list) -> int:
#        window = set()
#        max_size = 0
#        i, j, n = 0, 0, len(height)
#        for width in range(n, 1, -1):
#            start = n - width
#            while start >= 0:
#                print('------------')
#                print('start:'+ str(start))
#                print('start[]:'+ str(height[start]))
#                print('width:'+ str(width))
#                print('width[]:'+ str(height[start+width-1]))
#                print(self.calc_area(height[start],height[start+width-1], width))
#                current_max = self.calc_area(height[start],height[start+width-1], width)
#                start -= 1 
#                if current_max > max_size:
#                    max_size = current_max
#                print('currnet_max:', current_max)
#                print('------------')
#        return max_size
#
#    def calc_area(self, height_1:int, height_2:int, width:int) -> int:
#        print('height_1:'+ str(height_1))
#        print('height_2:'+ str(height_2))
#        print('width:'+ str(width))
#        if height_1 < height_2:
#            height = height_1
#        else:
#            height = height_2
#        print('height:'+ str(height))
#
#        if width != 1:
#            width -= 1
#        return height * width 
##これではtime  limit exceeded

class Solution(object):
    def maxArea(self, s):
        maxarea, l, r = 0, 0 , len(s) - 1
        while (l < r) :
            maxarea = max(maxarea, min(s[l], s[r]) * (r - l))
            if s[l] < s[r] :
                l+=1
            else:
                r-=1
        return maxarea


solution = Solution()
#print(solution.maxArea([1,8,6,2,5,4,8,3,7]))
print(solution.maxArea([1,2,4,3]))
