class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.linkdlist=[]
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        try:
            if self.linkdlist[index]:
                return self.linkdlist[index]
        except:
            return -1 

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.linkdlist.insert(0, val)
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.linkdlist.append(val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if len(self.linkdlist) >= index:
            self.linkdlist.insert(index, val)
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        try:
            if self.linkdlist[index]:
                del self.linkdlist[index]
        except:
            return
    
    def debug(self):
        print(self.linkdlist)
        

linkedList = MyLinkedList() 
linkedList.addAtHead(1)
linkedList.addAtTail(3)
linkedList.addAtIndex(1, 2);  
linkedList.get(1)            
linkedList.deleteAtIndex(1)
linkedList.get(1)           