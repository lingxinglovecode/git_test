
#本节是关于链表的算法


#0 设计链表
class ListNode:
    def __init__(self,x,next=None):
        self.val = x
        self.next = next

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
        for i in range(self.size):
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

#1.删除链表的倒数第N个节点
#给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

class Solution:

    #解法1：如果传入的是自定义的mylistnode，可以直接调用其中size属性和deleteAtIndex方法
    def removeNthFromEnd(self,head,n):
        index = head.size - n
        head.deleteAtIndex(index)
        return head

    #解法2：传入的是listnode的形式，需要获取其数量以及索引位置
    def removeNthFromEnd(self,head,n):
        last = head
        num = 0
        while last:
            num += 1
            last = last.next
        temp = ListNode(0,next=head)
        index = num - n
        pred = temp
        for _ in range(index):
            pred = pred.next
        pred.next = pred.next.next
        return temp.next

    #解法3：双指针
    def removeNthFromEnd(self,head,n):

        temp = ListNode(0,head)
        fast,slow = temp,temp
        num = 0
        while num != n and fast.next:
            fast = fast.next
            num += 1
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return temp.next

    #解法4：栈，先依次进栈，然后再出栈
    def removeNthFromEnd(self,head,n):
        temp = ListNode(0,head)
        stack = list()
        cur = temp
        while cur:
            stack.append(cur)
            cur = cur.next
        for i in range(n):
            stack.pop()
        prev = stack[-1]
        prev.next = prev.next.next
        return temp.next












if __name__ == '__main__':
    my_node = MyLinkedList()
    # my_node.addAtHead(2)
    my_node.addAtHead(1)
    # my_node.addAtTail(3)
    my_node.size

    list_node_flag = 1
    if list_node_flag:
        list_node_1 = ListNode(1)
        list_node_2 = ListNode(2)
        list_node_3 = ListNode(3)
        list_node_1.next = list_node_2
        list_node_2.next = list_node_3
    print(list_node_1)
    solution  = Solution()
    new_node = solution.removeNthFromEnd(list_node_1,1)
    a=2
