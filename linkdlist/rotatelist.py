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
            if node == None:
                break
            if node.val == headval:
                print('end cyclic list')
                break
        
        print('len:'+ str(length))
        print('end- print_all-------')
    

'''
https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1295/

'''
class Solution(object):
    def rotateRight(self, head:ListNode, k: int):
        # base cases
        if not head:
            return None
        if not head.next:
            return head
        
        # 現状のlistの最後の要素を見つけるのと、要素数のカウントを(n)する。
        old_tail = head
        n = 1
        while old_tail.next:
            old_tail = old_tail.next
            n += 1
        old_tail.next = head 

        # rotate後の最後の要素を見つける : (n - k % n - 1)番目の要素 右にローテートなので、最後の要素はマイナス1になる。
        # rotate後のhead要素を見つける (n - k % n)番目の要素
        new_tail = head
        for i in range(n - k % n - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        
        # リングにしたlistを切る
        new_tail.next = None
        
        return new_head


linkedlist = ListNode(1) 
listmaker = MyLinkedList()
linkedlist=listmaker.addAtTail(linkedlist,2)
linkedlist=listmaker.addAtTail(linkedlist,3)
linkedlist=listmaker.addAtTail(linkedlist,4)
linkedlist=listmaker.addAtTail(linkedlist,5)
listmaker.print_all(linkedlist)

#solution = Solution()
#res = solution.insert(linkedlist, 0)
#listmaker.print_cyclic(res)
#print(res)
