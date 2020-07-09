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
        https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1227/
        https://leetcode.com/articles/merged-two-sorted-lists/
        1->2->4, 1->3->4 のリストが２つだったとして順序としては
        1-1 と 2-1を比較 同じなので1-1にpointerがいくprev (小さい方にpointerが向く) 1
        1-1がprev, 1-2と2-1を比較、2-1にpointerがいく... 1
        2-1がprev, 1-2と2-2を比較、1-2にpointerがいく... 2
        1-2がprev, 1-3と2-2を比較、2-2にpointerがいく... 3
        2-2がprev, 1-3と2-3を比較、1-3にpointer街区 ....4
        
        
    '''
class Solution:
    def mergeTwoLists(self, l1, l2):
        # maintain an unchanging reference to node ahead of the return node.
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next            
            prev = prev.next

        # exactly one of l1 and l2 can be non-null at this point, so connect
        # the non-null list to the end of the merged list.
        prev.next = l1 if l1 is not None else l2

        return prehead.next



linkedlist1 = ListNode(1)
listmaker = MyLinkedList()
linkedlist1=listmaker.addAtTail(linkedlist1,2)
linkedlist1=listmaker.addAtTail(linkedlist1,4)

linkedlist2 = ListNode(1)
linkedlist2=listmaker.addAtTail(linkedlist2,3)
linkedlist2=listmaker.addAtTail(linkedlist2,4)
#listmaker.print_all(linkedlist1)
#listmaker.print_all(linkedlist2)
#print(linkedList.head.next.val)
solution = Solution()
res = solution.mergeTwoLists(linkedlist1, linkedlist2)
listmaker.print_all(res)
#print(res)


