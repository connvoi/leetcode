
#get(index) : Get the value of the index-th node in the linked list. If the index is invalid, return -1.
#addAtHead(val) : Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
#addAtTail(val) : Append a node of value val to the last element of the linked list.
#addAtIndex(index, val) : Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
#deleteAtIndex(index) : Delete the index-th node in the linked list, if the index is valid. 
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.size=0 
        self.head=ListNode(0)
        

    def get(self, index: int) -> int:
        if index < 0 or index > self.size:
            return -1
        
        node = self.head
        for _ in range(index+1):
            node = node.next
        
        return node.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)
        

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return 

        node = self.head
        for _ in range(index):
            node = node.next
        
        self.size += 1
        to_add = ListNode(val)
        to_add.next = node.next
        node.next = to_add
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return -1
        
        self.size -= 1
        node = self.head
        for _ in range(index):
            node = node.next
        
        node.next = node.next.next

class Solution:
    #firstとslowの２つのポインタをみて、リストが同じ値だった場合はそのlinkdlistがサイクルがあるとみなす。
    #同じリストがみつからなく、fastのリストがなくなった場合はサイクルがない
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next: 
            return False        

        slow, fast = head, head.next
        while slow != fast:
            if not fast or not fast.next: 
                return False
            slow, fast = slow.next, fast.next.next

        return True

#計算量
#
#list自体にサイクルがある場合はO(n)
#
#サイクルがある場合は、計算量の考え方としては2つのぽいんたの距離と、その距離を進む速度になって、
#fastポインタがslowポインタに追いつく速度。その速度差は１なので、
#イテレーションの数 = almost cyclic length K
#
#になるので、ワーストケースはO(N + K) = O(N)



