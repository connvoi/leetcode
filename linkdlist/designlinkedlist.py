class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.size=0
        self.head = ListNode(0)
        

    def get(self, index: int) -> int:
        # indexが正しい値かどうかをチェック
        if index < 0 or index >= self.size:
            return -1

        curr = self.head

        # index steps needed 
        # to move from sentinel node to wanted index
        # linkdlistを欲しいindexの番号まで進める。linkdlistは0からスタートなので1を+
        for _ in range(index + 1):
            curr = curr.next

        return curr.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size, val)
        
    def addAtIndex(self, index: int, val: int) -> None:

        """
        indexの指定がlinkdlistより大きい場合、何もしないでreturn 
        """
        if index > self.size:
            return 
        
        #sizeをプラス1にする
        self.size += 1

        # find predecessor of the node to be added
        # 挿入すべき場所のひとつ前のnodeを特定する。
        pred = self.head
        for _ in range(index):
            pred = pred.next

        #node to be added
        #追加すべきnodeのデータ作成(初期化)
        to_add = ListNode(val)
        #nextにpredecessorをとして特定したnodeを入れる。
        #predが次に指していた物に自分をいれてインサート完了
        to_add.next = pred.next
        pred.next = to_add

        
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        #サイズのチェック
        if index < 0 or index >= self.size:
            return -1

        #デリートなのでひとつ削除するためにサイズを削る
        self.size-= 1
        pred =self.head
        #指定されたインデックスまでポインタを進める
        for _ in range(index):
            pred = pred.next
        
        #指定されたインデックスのnextを次の次に指定すればリストから消える
        pred.next = pred.next.next


linkedList = MyLinkedList() 
linkedList.addAtHead(1)
linkedList.addAtTail(3)
linkedList.addAtIndex(1, 2);  
linkedList.get(1)            
linkedList.deleteAtIndex(1)
linkedList.get(1)           