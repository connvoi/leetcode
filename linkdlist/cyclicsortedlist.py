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
    
    def connectTailtoHead(self, node: ListNode) -> ListNode:
        head = node
        while node.next != None:
            node = node.next
        
        node.next = head

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
    
    def print_cyclic(self, node:ListNode) -> None:
        print('start-print_all-------')
        headval = node.val
        length =0
        while node != None:
            print(node.val)
            node = node.next
            length+=1
            if node.val == headval:
                print('end cyclic list')
                break;
        
        print('len:'+ str(length))
        print('end- print_all-------')
    
        

"""
https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1226/

case1: 数字の間に入れる場合 5 と 7 の間に入れるなど
case2: listの最大値で最後に入れる場合 1~9のlistでinsertが10
case3: 0を入れる場合(無条件でhead)
case4: list自体がない場合は追加
"""

class Solution:
    def insert(self, head: ListNode, insertVal: int):
        if head == None:
            node = ListNode(insertVal)
            node.next = None
            return node

        node = head


        while node != None:
            if node.val < insertVal and insertVal < node.next.val:
                to_add = ListNode(insertVal) 
                to_add.next = node.next
                node.next = to_add
                node = node.next
                break
            node = node.next
            if node.val == head.val:
                break
        return head


linkedlist = ListNode(3)
listmaker = MyLinkedList()
linkedlist=listmaker.addAtTail(linkedlist,4)
linkedlist=listmaker.addAtTail(linkedlist,1)
linkedlist=listmaker.connectTailtoHead(linkedlist)
#listmaker.print_cyclic(linkedlist)


solution = Solution()
res = solution.insert(linkedlist, 2)
listmaker.print_cyclic(res)
#print(res)


