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
    
        
#初期の問題はlinkedlistの開始点が0で最終店がNoneだったんだけど、その前提がなくなっているので、開始店からnodeの1番目の数字が入っていないとだめみたい。
#んなばかな。
class Solution:
    '''
        https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1206/
    '''
    def reverseList(self, node: ListNode) -> ListNode:
        head = None
        
        while node != None:
            if head == None:
                head = ListNode(node.val)
                head.next = None
            else:
                to_add = ListNode(node.val)
                to_add.next = head
                head = to_add
            node = node.next
        
        return head
    
    '''
        https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1207/
    '''
    def removeElements(self, node: ListNode, val:int) -> ListNode:
        print('--- debug ---')
        head = node
        pred = None
        
        while node != None:
            print(node.val)
            if node.val == val:
                if pred != None:
                    print('pred')
                    print(node.next)
                    pred.next = node.next
                else:
                    '''
                    node.val == val and pred is Noneのときはいま見ているnodeがheadになる->predもNoneにしないといけない
                    '''
                    print('pred is none')
                    head = node.next
                    pred = node
            else:
                pred = node

            node = node.next
        
        print('--- debug end ---')
        return head




linkedlist = ListNode(1)
listmaker = MyLinkedList()
linkedlist=listmaker.addAtTail(linkedlist,1)
#linkedlist=listmaker.addAtTail(linkedlist,2)
#linkedlist=listmaker.addAtTail(linkedlist,6)
#linkedlist=listmaker.addAtTail(linkedlist,3)
#linkedlist=listmaker.addAtTail(linkedlist,4)
#linkedlist=listmaker.addAtTail(linkedlist,5)
#linkedlist=listmaker.addAtTail(linkedlist,6)
#listmaker.print_all(linkedlist)
#print(linkedList.head.next.val)
solution = Solution()
#res = solution.reverseList(linkedlist)
res = solution.removeElements(linkedlist,1)
listmaker.print_all(res)


