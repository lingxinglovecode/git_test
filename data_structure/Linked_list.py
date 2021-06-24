
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

    #递归的应用：逆序输出链表中的值
    def printList_reverse(self,head):
        if head == None:
            return
        self.printList_reverse(head.next)
        print(head.val)




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

    #2.反转一个单链表

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

    #方法2：递归
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

    #4.判断一个链表是否为回文链表


    #方法1：栈
    def isPalindrome(self,head):
        # 判断长度
        len_list = 0
        len_head = head
        while len_head:
            len_list += 1
            len_head = len_head.next

        stack = list()
        start = head
        mid = len_list // 2
        for _ in range(mid):
            stack.append(start.val)
            start = start.next
        mid_node = start.next if len_list%2 != 0 else start
        for _ in range(mid):
            if stack.pop() != mid_node.val:
                return False
            mid_node = mid_node.next
        return True

    #方法2：双指针
    def isPalindrome(self,head):
        def first_half_end(head):
            slow = head
            fast = head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def reverse_List(head):
            cur = head
            while cur.next:
                temp = ListNode(cur.next.val)
                cur.next = cur.next.next
                temp.next = head
                head = temp
            return head

        if head == None or head.next == None:
            return True
        first_half_end = first_half_end(head)
        second_half_start = reverse_List(first_half_end.next)

        flag = True
        first = head
        second = second_half_start
        while second:
            if first.val != second.val:
                flag = False
                break
            first = first.next
            second = second.next
        first_half_end.next = reverse_List(second_half_start)
        return flag

    #方法3：递归
    def isPalindrome(self,head):
        self.temp = head
        def Checkfrombottom(head):
            if head == None:
                return True
            result = Checkfrombottom(head.next) and head.val == self.temp.val
            self.temp = self.temp.next
            return result
        return Checkfrombottom(head)

    #5.判断一个链表是不是环形链表

    #方法1：双指针
    def hasCycle(self, head):
        slow = head
        if not head or not head.next or not head.next.next:
            return False
        fast = head.next.next
        while fast.next and fast.next.next:
            if slow == fast  or fast.next == slow:
                return True
            slow = slow.next
            fast = fast.next.next
        return False

    #方法2：哈希表
    def hasCycle(self, head):
        hashmap = dict()
        move = head
        if not move or not move.next:
            return False
        while move:
            if move in hashmap:
                return True
            hashmap[move] = 1
            move = move.next
        return False


    #6.两数相加
    #https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xvw73v/
    def addTwoNumbers(self, l1, l2) :
        res = ListNode(0)
        head = res
        while l1 and l2:
            add_val = l1.val + l2.val
            res.val = res.val + add_val
            if res.val >= 10:
                remain = res.val % 10
                carry = res.val // 10
                res.val = remain
                temp = ListNode(0)
                res.next = temp
                res = res.next
                res.val = carry
                l1 = l1.next
                l2 = l2.next
                continue
            l1 = l1.next
            l2 = l2.next
            if l1 or l2:
                temp = ListNode(0)
                res.next = temp
                res = res.next
        while l1:
            res.val = l1.val + res.val

            if res.val >= 10:
                remain = res.val % 10
                carry = res.val // 10
                res.val = remain
                temp = ListNode(0)
                res.next = temp
                res = res.next
                res.val = carry
                l1 = l1.next
                continue

            l1 = l1.next
            if l1:
                temp = ListNode(0)
                res.next = temp
                res = res.next
        while l2:
            res.val = l2.val + res.val

            if res.val >= 10:
                remain = res.val % 10
                carry = res.val // 10
                res.val = remain
                temp = ListNode(0)
                res.next = temp
                res = res.next
                res.val = carry
                l2 = l2.next
                continue
            l2 = l2.next
            if l2:
                temp = ListNode(0)
                res.next = temp
                res = res.next
        return head


    def addTwoNumbers(self,l1,l2):
        head = ListNode(x=None)
        node = head
        carry = 0
        while l1 or l2:

            add_1 = l1.val if l1 else 0
            add_2 = l2.val if l2 else 0
            add_res = add_1+add_2+carry

            carry = add_res // 10
            num = add_res % 10

            if head.val != None:
                node.next = ListNode(num)
                node = node.next
            else:
                node.val = num

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry>0:
            node.next = ListNode(carry)
        return head


    #7.奇偶链表
    #https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xvdwtj/
    def oddEvenList(self, head) :
        odd_head = head
        even_head = head.next
        node = head
        count = 0
        while node.next.next:
            temp = node.next
            node.next  = node.next.next
            count += 1
            node = temp
        if count%2 == 0:
            odd_tail = node
            odd_tail.next = even_head
        else:
            even_tail = node
            odd_tail = node.next
            odd_tail.next = even_head
            even_tail.next = None
        return odd_head


    #8.相交链表
    #方法1：哈希表
    def getIntersectionNode(self, headA,headB) :
        node_A = headA
        node_B = headB
        node_dict = dict()
        while node_A:
            node_dict[node_A] = 1
            node_A = node_A.next
        while node_B:
            if node_B in node_dict:
                return node_B.val
            node_B = node_B.next
        return None

    #方法2：根据链表长度找到可能的相交节点
    def getIntersectionNode(self,headA,headB):
        node_A = headA
        node_B = headB
        len_A  = 0
        len_B = 0
        while node_A:
            len_A += 1
            node_A = node_A.next
        while node_B:
            len_B += 1
            node_B = node_B.next
        first= headA
        second = headB
        if len_A<len_B:
            move = len_B-len_A
            while move:
                second = second.next
                move -= 1
        elif len_A>len_B:
            move = len_A-len_B
            while move:
                first = first.next
                move -= 1
        while first:
            if first == second:
                return first
            first = first.next
            second = second.next
        return None















































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
        list_node_3 = ListNode(2)
        list_node_4 = ListNode(1)
        list_node_1.next = list_node_2
        list_node_2.next = list_node_3
        list_node_3.next = list_node_4

        list_1 = ListNode(1)
        list_2 = ListNode(2)
        list_3 = ListNode(3)
        # list_4 = ListNode(4)
        list_1.next = list_2
        list_2.next = list_3
        # list_3.next = list_4

    # print(list_node_1)
    solution  = Solution()
    # new_node = solution.removeNthFromEnd(list_node_1,1)
    # solution.reverseList(list_node_1)
    # new_list = solution.mergeTwoLists(list_node_1,list_2)
    # a=2
    # solution.isPalindrome(list_node_1)
    # solution.printList_reverse(list_2)
    # solution.hasCycle(list_node_1)

    # solution.addTwoNumbers(list_1,list_2)

    #7奇偶链表
    solution.oddEvenList(list_1)
