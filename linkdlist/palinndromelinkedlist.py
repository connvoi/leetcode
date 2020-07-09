class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList: 

    def get(self, node: ListNode, index: int) -> int:
        for _ in range(index+1):
            node = node.next
        
        return node.val


    def addAtTail(self, node: ListNode, val: int) -> ListNode:
        head = node
        while node.next != None:
            node = node.next
        
        to_add = ListNode(val)
        node.next = to_add

        return head
        

    def print_all(self, node:ListNode) -> None:
        print('start-print_all-------')
        length =0
        while node != None:
            print(node.val)
            node = node.next
            length+=1
        
        print('len:'+ str(length))
        print('end- print_all-------')
    
        
class Solution:
    '''
        https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1209/
    '''
    def isPalindrome(self, node: ListNode) -> bool:
        sentence = [] 
        pred = None
        count = 0

        while node != None:
            sentence.append(node.val)

            pred = node.val
            node=node.next
            count+=1

        #case even
        center = int(count/2) 
        if count % 2 != 0 :
            #odd
            if sentence[0:center+1] == list(reversed(sentence[center:count])):
                return True
        else:
            if sentence[0:center] == list(reversed(sentence[center:count])):
                return True

        return False

#これ頭いい。
#class Solution:
#    def isPalindrome(self, head: ListNode) -> bool:
#    vals = []
#    current_node = head
#    while current_node is not None:
#        vals.append(current_node.val)
#        current_node = current_node.next
#    return vals == vals[::-1]


linkedlist = ListNode(1)
listmaker = MyLinkedList()
linkedlist=listmaker.addAtTail(linkedlist,2)
#linkedlist=listmaker.addAtTail(linkedlist,3)
linkedlist=listmaker.addAtTail(linkedlist,2)
linkedlist=listmaker.addAtTail(linkedlist,1)
#linkedlist=listmaker.addAtTail(linkedlist,6)
#linkedlist=listmaker.addAtTail(linkedlist,4)
#linkedlist=listmaker.addAtTail(linkedlist,7)
#listmaker.print_all(linkedlist)
#print(linkedList.head.next.val)
solution = Solution()
res = solution.isPalindrome(linkedlist)
#res = solution.removeElements(linkedlist,1)
print(res)


