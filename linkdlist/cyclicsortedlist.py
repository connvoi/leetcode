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
    
        

"""
https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1226/

case1: 数字の間に入れる場合 5 と 7 の間に入れるなど
case2: listの最大値で最後に入れる場合 1~9のlistでinsertが10
case3: 0を入れる場合(無条件でhead)
case4: list自体がない場合は追加
"""
class Solution:
    def insert(self, head: ListNode, insertVal: int) -> 'Node':
        if not head:
            head = ListNode(insertVal)
            head.next = head
            return head
        
        curr = head

        while True:
            #currentより大きくnextより小さい->listに挿入する
            if curr.val <= insertVal <= curr.next.val:
                break
            
            # last element
            if curr.val>curr.next.val:
                #currentより大きく、nextよりも大きい->最後のエレメント
                if curr.val <= insertVal >= curr.next.val:
                    break
                #currentとnextより小さい->最初のエレメント
                #cyclicなので最初と最後は一緒
                elif curr.val >= insertVal <= curr.next.val:
                    break
                    
            curr = curr.next 
            # all elements are equal
            if curr == head:
                break

        #new_nodeで作成
        new_node = ListNode(insertVal)
        #tmpに入れる
        tmp = curr.next
        #currentのnextにnewを入れる
        curr.next = new_node
        #new_nodeのnextにtmpを入れる
        new_node.next = tmp
        #linkedlistは入れたときにtmpなりに確保しておくとheadを移せる。忘れがちなので忘れないようにする。
        return head


linkedlist = ListNode(3)
listmaker = MyLinkedList()
linkedlist=listmaker.addAtTail(linkedlist,4)
linkedlist=listmaker.addAtTail(linkedlist,1)
linkedlist=listmaker.connectTailtoHead(linkedlist)
#listmaker.print_cyclic(linkedlist)


solution = Solution()
res = solution.insert(linkedlist, 0)
listmaker.print_cyclic(res)
#print(res)


