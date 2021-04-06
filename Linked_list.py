
#本节是关于链表的算法


#0 设计链表
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = ListNode(0)

    def get(self,index):
        #if index is invalid
        if index<0 or index>=self.size:
            return -1

        curr = self.head
        for _ in range(index+1):
            curr = curr.next
        return curr.val


    def addAtHead(self,val):
        curr = ListNode(val)
        curr.next = self.head.next
        self.head.next = curr
        self.size += 1

    def addAtTail(self,val):
        tail = self.head
        for i in range(self.size+1):
            tail = tail.next
        tail_node = ListNode(val)
        tail.next = tail_node
        self.size += 1

    def addAtIndex(self,index,val):
        if index > self.size:
            return
        if index < 0:
            index = 0
        to_add = ListNode(val)
        pred = self.head
        for _ in range(index):
            pred = pred.next
        to_add.next = pred.next
        pred.next = to_add
        self.size += 1

    def deleteAtIndex(self,index):
        if index < 0 or index >= self.size:
            return
        pred = self.head
        for _ in range(index):
            pred = pred.next
        pred.next = pred.next.next
        self.size -= 1

















if __name__ == '__main__':
    my_node = MyLinkedList()
    my_node.addAtHead(10)
    my_node.addAtTail(30)
    print(my_node)
