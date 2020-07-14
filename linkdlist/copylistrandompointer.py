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
https://leetcode.com/articles/copy-list-with-random-pointer/
'''
class Solution(object):
    def __init__(self):
        # 一度出現したnodeを覚えておく用のhash
        self.visitedHash = {}

    def copyRandomList(self, head):

        if head == None:
            return None

        # 一回処理したノードが出てきた場合は、同じノードを返す
        # ランダムポインタで同じリストを指定されたときにそのものを返すため
        if head in self.visitedHash:
            return self.visitedHash[head]

        # 同じnode.valをもつNodeを一つ作る,next,randomはNone
        node = Node(head.val, None, None)

        # 作成したnodeをhashに保存する。
        self.visitedHash[head] = node

        # Recursively copy the remaining linked list starting once from the next pointer and then from the random pointer.
        # Thus we have two independent recursive calls.
        # Finally we update the next and random pointers for the new node created.

        # ランダムポインタ、nextポインタを再起処理でポインタを進めていく
        # nextの方で全リストをたどり、randamの方はrandamめぐりが終わるまで回す(この問題の場合cyclicはない前提あったとしても同じノードたどると止まるので大丈夫)
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)

        return node
        
linkedlist = ListNode(3) listmaker = MyLinkedList()
linkedlist=listmaker.addAtTail(linkedlist,4)
linkedlist=listmaker.addAtTail(linkedlist,1)
linkedlist=listmaker.connectTailtoHead(linkedlist)
#listmaker.print_cyclic(linkedlist)


#solution = Solution()
#res = solution.insert(linkedlist, 0)
#listmaker.print_cyclic(res)
#print(res)


