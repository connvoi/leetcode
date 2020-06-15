
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



linkedList = MyLinkedList() 
linkedList.addAtHead(1)
linkedList.addAtTail(3)
linkedList.addAtIndex(1, 2);  
linkedList.get(1)            
linkedList.deleteAtIndex(1)
linkedList.get(1)           