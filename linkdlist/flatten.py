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
    
# flattenでchildありの場合のlinkedlistの全走破をまとめる。
        
class Solution:
    def addTwoNumbers(self, l1:ListNode, l2:ListNode) -> ListNode:
        # maintain an unchanging reference to node ahead of the return node.
        node = ListNode(-1) 
        head = node
        l1num=''
        l2num=''
        while l1:
            l1num = str(l1.val) + l1num
            l1=l1.next

        while l2:
            l2num = str(l2.val) + l2num
            l2=l2.next
        
        total = int(l1num) + int(l2num)
        total = str(total)

        for i in range(len(total)-1,-1,-1):
            to_add=ListNode(int(total[i]))
            node.next=to_add
            node=node.next
            

        return head.next



linkedlist1 = ListNode(2)
listmaker = MyLinkedList()
linkedlist1=listmaker.addAtTail(linkedlist1,4)
linkedlist1=listmaker.addAtTail(linkedlist1,3)

linkedlist2 = ListNode(5)
linkedlist2=listmaker.addAtTail(linkedlist2,6)
linkedlist2=listmaker.addAtTail(linkedlist2,4)
#listmaker.print_all(linkedlist1)
#listmaker.print_all(linkedlist2)
#print(linkedList.head.next.val)
solution = Solution()
res = solution.addTwoNumbers(linkedlist1, linkedlist2)
listmaker.print_all(res)
#print(res)


