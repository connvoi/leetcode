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

'''
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

node numberをグループ化するので、node.valをグループ化したダメです!!!!
'''
class Solution:
    '''
        https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1208/
    '''
    def oddEvenList(self, node: ListNode) -> ListNode:
        print('--- debug ---')
        oddevenhead = None
        oddevenlist = None
        evenlist = None
        evenhead = None
        oddList = None
        oddhead = None
        count = 1

        if node == None:
            return None

        while node != None:
            if count == 1:
                oddevenlist = ListNode(node.val)
                oddevenhead = oddevenlist
                count+=1
                node = node.next
                continue

            if count == 2:
                evenlist = ListNode(node.val)
                evenhead = evenlist
                count+=1
                node = node.next
                continue

            if count == 3:
                oddlist = ListNode(node.val)
                oddhead = oddlist
                count+=1
                node = node.next
                continue
                
            if count % 2 == 0:
                to_add = ListNode(node.val)
                evenlist.next = to_add
                evenlist = evenlist.next
            else:
                to_add = ListNode(node.val)
                oddlist.next = to_add
                oddlist = oddlist.next

            node = node.next
            count+=1
        
        if count == 2:
            return oddevenhead
        elif count == 3:
            oddevenhead.next = evenhead
        else:
            oddevenhead.next = oddhead
            oddlist.next = evenhead
        
        print('--- debug end ---')
        return oddevenhead




linkedlist = ListNode(2)
listmaker = MyLinkedList()
#linkedlist=listmaker.addAtTail(linkedlist,1)
#linkedlist=listmaker.addAtTail(linkedlist,3)
#linkedlist=listmaker.addAtTail(linkedlist,5)
#linkedlist=listmaker.addAtTail(linkedlist,6)
#linkedlist=listmaker.addAtTail(linkedlist,4)
#linkedlist=listmaker.addAtTail(linkedlist,7)
#listmaker.print_all(linkedlist)
#print(linkedList.head.next.val)
solution = Solution()
res = solution.oddEvenList(linkedlist)
#res = solution.removeElements(linkedlist,1)
listmaker.print_all(res)


