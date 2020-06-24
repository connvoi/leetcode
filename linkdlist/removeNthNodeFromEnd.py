class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int):
        length = 0
        while head.next:
            length+=1

        p = length - n

        i = 0
        while  i> p:
            head


        return True

#ローカルでlinklistを作れるようになららいと問題文がうまく溶けなくね？
#listを渡してlinklistの形にできるものを作る

node = Listnode()

test = [1,2,3,4,5]
for i in test:
