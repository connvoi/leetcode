#Given a string, find the length of the longest substring without repeating characters.
#
# ex1
#Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
#
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
#Input: "pwwkew"
#Output: 3
#Explanation: The answer is "wke", with the length of 3. 
#             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
# TODO
#https://dev.classmethod.jp/articles/longest-substring-without-repeating-characters/


#class Solution(object):
#    def lengthOfLongestSubstring(self, s):
#        current_max = 0
#        result_max = 0
#        for i in range(len(s)):
#            dic = []
#            current_max = 0
#            for j in range(i,len(s)):
#
#                if s[j] not in dic:
#                    current_max += 1
#                    dic.append(s[j])
#                else:
#                    current_max = 0
#                    dic = []
#                
#                
#                if current_max > result_max:
#                    result_max = current_max
#        return result_max

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        max_size = 0
        i, j, n = 0, 0, len(s)
        while i < n and j < n:
            #windowのdictないにs[j]がない時はwindowに追加し、ある時はdiscardで捨て、i++でウインドウの開始点をずらす。
            #これを文字列に対してやっていく。
            if s[j] not in window:
                window.add(s[j])
                max_size = max(len(window), max_size)
                j += 1
            else:
                window.discard(s[i])
                i += 1
        return max_size

solution = Solution()
#print(solution.lengthOfLongestSubstring('abcabcbb'))
#print(solution.lengthOfLongestSubstring('bbbbb'))
print(solution.lengthOfLongestSubstring('bbbbbbb'))
#print(solution.lengthOfLongestSubstring('pwwkew'))
print(solution.lengthOfLongestSubstring('dvdf'))