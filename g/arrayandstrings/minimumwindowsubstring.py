#https://leetcode.com/explore/interview/card/google/59/array-and-strings/345/

"""
文字列SとTがあたえられて、Sの中にTの文字すべてが含まれている最小のすインドを見つける。
例
Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
"""
import collections

class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not t or not s:
            return ""

        # stringの書く文字列が何回出てくるかをカウントする abbbcc -> {a,1}, {b,3}, {c,2} とかする
        dict_t = collections.Counter(t)

        # ユニークな文字の長さを求める
        required = len(dict_t)

        # left and right pointer
        l, r = 0, 0

        # formed is used to keep track of how many unique characters in t are present in the current window in its desired frequency.
        # e.g. if t is "AABC" then the window must have two A's, one B and one C. Thus formed would be = 3 when all these conditions are met.
        """
        formedはwindow内のユニークなキャラクターがどれくらいあるかを見ている。
        例えば t=AABCだったばあい、 Aが2, B,Cが1で、formed=3となるformedが求める数になるときを探す。
        """
        formed = 0

        #Dictionary which keeps a count of all the unique characters in the current window.
        #現在のウインドウ内のユニークな文字数のカウントをする
        window_counts = {}

        # ans tuple of the form (window length, left, right)
        # formのタプル float('inf')は無限大(infinity)
        ans = float("inf"), None, None

        while r < len(s):

            # Add one character from the right to the window
            # 1文字ずつwindow_countを取る
            character = s[r]
            #文字がなかったら(はじめは空なので絶対に1になる)1で同じ文字だったら+=1になる
            window_counts[character] = window_counts.get(character, 0) + 1

            # If the frequency of the current character added equals to the desired count in t then increment the formed count by 1.
            # 現在の文字がdict_tの中にあり、カウント数が同じ場合formedに+1をする
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1

            # Try and contract the window till the point where it ceases to be 'desirable'.
            # 求めるケースになるまでformed==requiered ループをする
            # leftponterをrightpointerまですすめながら処理をする
            while l <= r and formed == required:
                character = s[l]

                # Save the smallest window until now.
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                # The character at the position pointed by the `left` pointer is no longer a part of the window.
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1

                # Move the left pointer ahead, this would help to look for a new window.
                l += 1    

            # Keep expanding the window once we are done contracting.
            r += 1    
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]


solution = Solution()
print(solution.minWindow("ADOBECODEBANC", "ABC"))