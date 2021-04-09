
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

    #2.翻转一个单链表

    #方法1：栈的思想。先把链表中元素存储，然后再重新排序。
    def reverseList(self,head):
        if not head:
            return head
        stack = list()
        cur = head
        while cur:
            stack.append(ListNode(cur.val))
            cur = cur.next
        rev_head = stack.pop()
        rev_last = rev_head
        while len(stack) != 0:
            rev_last.next = stack.pop()
            rev_last = rev_last.next
        return rev_head

    #方法2：依次遍历并将每一个元素移动位置至开头
    def reverseList(self,head):
        if not head:
            return head
        cur = head
        while cur.next:
            temp = ListNode(cur.next.val)
            cur.next = cur.next.next
            temp.next = head
            head = temp
        return head

    #方法3：递归的思想
    def reverseList(self,head):
        if head == None or head.next == None:
            return head
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head


    #3.合并两个有序列表
    #将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

    #方法1：双指针
    def mergeTwoLists(self, l1, l2):
        one = l1
        two = l2
        new_list_head = ListNode(0)
        new_node = new_list_head
        while one or two:
            if one and (not two or one.val <= two.val):
                value = one.val
                one = one.next
            elif two:
                value = two.val
                two = two.next
            new_node.next = ListNode(value)
            new_node = new_node.next
        return new_list_head.next


    def mergeTwoLists(self,l1,l2):

        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2


































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
        list_node_4 = ListNode(4)
        list_node_1.next = list_node_2
        list_node_2.next = list_node_3
        list_node_3.next = list_node_4

        list_2 = ListNode(2)
        list_2.next = ListNode(3)
        list_2.next.next = ListNode(4)
    print(list_node_1)
    solution  = Solution()
    # new_node = solution.removeNthFromEnd(list_node_1,1)
    # solution.reverseList(list_node_1)
    new_list = solution.mergeTwoLists(list_node_1,list_2)
    a=2
