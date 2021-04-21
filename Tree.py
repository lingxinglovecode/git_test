
#本文主要涵盖与树这一数据结构相关的算法

    #0 树的基本概念与基本操作
    #树是一种包含节点的值和其所有子节点列表的数据结构，在树中最为常见的是二叉树，二叉树之中每一个节点至多包含两个子节点
    #其中两个节点成为左子树和右子树
import collections


class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def list_to_tree(tree_list):
    if len(tree_list) == 0:
        return None
    queue = collections.deque()
    length = len(tree_list)
    root = TreeNode(tree_list[0])
    queue.append(root)
    i = 1
    while i < length:
        node = queue.popleft()
        if node:
            node.left = TreeNode(tree_list[i]) if tree_list[i] else None
            queue.append(node.left)
            i = i+1
            if i < length:
                node.right = TreeNode(tree_list[i]) if tree_list[i] else None
                queue.append(node.right)
                i = i+1
    return root

















    ## 树的操作基础————遍历

class Solution:

    def __init__(self):
        self.max_depth = 0

    # 0-1前序遍历： 前序遍历从根节点开始访问，然后是左子树，最后是右子树
    #方法1：递归
    def preorderTraversal(self,root):
        if root == None:
            return []
        return [root.val]+self.preorderTraversal(root.left)+self.preorderTraversal(root.right)
    #方法2：栈
    def preorderTraversal(self,root):
        node = root
        stack = list()
        result =list()
        if not root:
            return []
        while stack or node:
            while node:
                result.append(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        return result

    #方法3：Morris 遍历
    def preorderTraversal(self,root):
        if root == None:
            return []
        list = []
        cur1 = root
        cur2 = None

        while cur1:
            cur2 = cur1.left
            if cur2:
                while (cur2.right != None) and (cur2.right != cur1):
                    cur2 = cur2.right
                if cur2.right == None:
                    cur2.right = cur1
                    list.append(cur1.val)
                    cur1 = cur1.left
                    continue
                elif cur2.right == cur1:
                    cur2.right = None
            else:
                list.append(cur1.val)
            cur1 = cur1.right
        return list

    # 0-2中序遍历： 中序遍历先对左子树进行遍历然后是根节点，最后是右子树

    #方法1：递归
    def inorderTraversal(self, root):
        if root == None:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

    #方法2：栈
    def inorderTraversal(self,root):
        if root == None:
            return []
        node = root
        stack = list()
        tree_list = list()

        while node or stack:
            cur = node
            while cur:
                stack.append(cur)
                cur = cur.left
            out = stack.pop()
            tree_list.append(out.val)
            node = out.right
        return tree_list

    #方法3：Morris遍历
    def inorderTraversal(self,root):
        if root == None:
            return []
        cur1 = root
        tree_list = list()


        while cur1:
            cur2 = cur1.left
            if cur2 != None:

                #移动到左子树的最后侧节点并建立连接
                while cur2.right and cur2.right != cur1:
                        cur2 = cur2.right
                if cur2.right == None:#没有连接的话建立连接
                    cur2.right = cur1
                    cur1 = cur1.left
                elif cur2.right == cur1: #如果已有连接就删除
                    tree_list.append(cur1.val)
                    cur1 = cur1.right
                    cur2.right = None

            else:
                tree_list.append(cur1.val)
                cur1 = cur1.right
        return tree_list

    #0-3 后序遍历
    #后序遍历先遍历左子树，然后右子树，最后根节点

    #方法1：递归
    def postorderTraversal(self,root):
        if root == None:
            return []
        return   self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

    #方法2：栈
    def postorderTravelsal(self,root):
        if root == None:
            return []
        stack = list()
        result = list()

        node = root
        prec = None
        while node or stack:
            while node != None:
                stack.append(node)
                node = node.left
            node = stack.pop()
            #当右侧没有节点或者当前节点已经被遍历过时输出值
            if (not node.right) or (node.right == prec):
                result.append(node.val)
                prec = node
                node = None
            else:
                stack.append(node)
                node = node.right
        return result

    #方法3：Morris遍历
    def postorderTravelsal(self, root):

        def addPath(node):
            count = 0
            while node:
                result.append(node.val)
                node = node.right
                count = count + 1
            i = len(result)-count
            j = len(result)-1
            while i<j:
                result[i],result[j] = result[j],result[i]
                i += 1
                j -= 1

        if root == None:
            return []
        cur1 = root
        result = list()

        while cur1:
            cur2 = cur1.left
            if cur2:
                while cur2.right and cur2.right != cur1:
                    cur2 = cur2.right
                if cur2.right == None:
                    cur2.right = cur1
                    cur1 = cur1.left
                    continue
                else:
                    cur2.right = None
                    addPath(cur1.left)
            cur1 = cur1.right
        addPath(root)
        return result

    #效率更低，因为每次都创建一个临时列表
    def postorderTravelsal(self, root):

        def save_list( node,result):
            temp_list = list()
            while node:
                temp_list.append(node.val)
                node = node.right
            temp_list.reverse()
            result = result + temp_list
            return result
        if root == None:
            return []
        cur1 = root
        result = list()

        while cur1:
            cur2 = cur1.left
            if cur2:
                while cur2.right and cur2.right != cur1:
                    cur2 = cur2.right
                if cur2.right == None:
                    cur2.right = cur1
                    cur1 = cur1.left
                    continue
                else:
                    cur2.right = None
                    result = save_list(cur1.left,result)
            cur1 = cur1.right
        result = save_list(root,result)
        return result

    #0.4层序遍历
    #方法1：队列
    def levelOrder(self, root: TreeNode):
        if root == None:
            return []
        queue = collections.deque()
        temp_queue = collections.deque()
        queue.append(root)
        result = []
        temp_res = []
        while queue:
            node = queue.popleft()
            temp_res.append(node.val)
            if node.left:
                temp_queue.append(node.left)
            if node.right:
                temp_queue.append(node.right)
            if not queue:
                result = result + [temp_res]
                queue = temp_queue
                temp_res = []
                temp_queue = collections.deque()
        return result

    #方法2：递归
    def levelOrder(self, root: TreeNode):
        result = [[]]
        def add_elements(root,level):

            if root and len(result) == level-1:
                result.append([])
            if len(result) >= level:
                result[level-1].append(root.val)
            if root.left:
                add_elements(root.left,level+1)
            if root.right:
                add_elements(root.right,level+1)
            return result

        if root == None:
            return []
        return add_elements(root,1)

    #1.二叉树的最大深度

    #方法1：递归
    def maxDepth(self, root: TreeNode) :
        cur_depth = 0
        max_depth = 0
        def count_cur_depth(root, cur_depth):
            nonlocal max_depth
            if cur_depth > max_depth:
                max_depth = cur_depth
            if root.left:
                count_cur_depth(root.left,cur_depth+1)
            if root.right:
                count_cur_depth(root.right,cur_depth+1)
            return max_depth
        if root == None:
            return cur_depth
        return count_cur_depth(root,1)

    def maxDepth(self, root: TreeNode):
        if root == None:
            return 0
        return max(self.maxDepth(root.left)+1,self.maxDepth(root.right)+1)

    #方法2：栈
    def maxDepth(self, root: TreeNode):
        if root == None:
            return 0
        stack = list()
        temp_stack = list()
        stack.append(root)
        depth = 0
        while stack or temp_stack:
            node = stack.pop()
            if node.left:
                temp_stack.append(node.left)
            if node.right:
                temp_stack.append(node.right)
            if not stack:
                depth = depth + 1
                stack = temp_stack
                temp_stack = list()
        return depth


    #2. 验证二叉搜索树的有效性
    # 一个有效的二叉搜索树其左子树应该小于根节点，右子树大于根节点

    #方法1.递归中序遍历判断
    def isValidBST(self, root: TreeNode) :
        def inorder(root):
            if root == None:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)
        inorder_list = inorder(root)
        for i in range(len(inorder_list)-1):
            if inorder_list[i+1] < inorder_list[i]:
                return False
        return True
    #方法2.栈中序遍历判断
    def isValidBST(self, root: TreeNode):
        if root == None:
            return True
        stack = list()
        node = root
        temp = None
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            cur = stack.pop()
            if temp != None and cur.val <= temp:
                return False
            temp = cur.val
            node = cur.right
        return True
    #方法3 直接递归判断
    def isValidBST(self,root):
        def isvalid(root,min=float('-inf'),max=float('inf')):
            if root == None:
                return True
            if root.val <= min or root.val >= max:
                return False
            return isvalid(root.left,min=min,max=root.val) and isvalid(root.right,min=root.val,max=max)
        return  isvalid(root)

    #3.验证一个二叉树是否是对称的

    #方法1：递归遍历后比较
    def isSymmetric(self, root: TreeNode) :
        if root == None:
            return True
        if not root.left and not root.right:
            return True
        def preorder(root):
            if root == None:
                return ['None']
            return [root.val] + preorder(root.left) + preorder(root.right)
        def reverse_order(root):
            if root == None:
                return ['None']
            return [root.val] + reverse_order(root.right) + reverse_order(root.left)
        left_node_list = preorder(root.left)
        right_node_list = reverse_order(root.right)
        if left_node_list == right_node_list:
            return True
        return False
    #方法2：直接递归
    def isSymmetric(self, root: TreeNode):
        if root == None:
            return True
        def symmetric(left,right):
            if left == None and right == None:
                return True
            if left and right:
                if left.val == right.val:
                    return symmetric(left.left,right.right) and symmetric(left.right,right.left)
            return False
        return symmetric(root.left,root.right)

    ##4.将有序数组转换为二叉搜索树

    #方法1：递归，每次将列表中间的值作为根节点
    def sortedArrayToBST(self,nums):
        if nums == []:
            return None
        length = len(nums)
        mid = length // 2  #得到中间数对应的序号
        root = TreeNode(nums[mid])
        if nums[:mid] != []:
            root.left = self.sortedArrayToBST(nums[:mid])
        if nums[mid+1:] != []:
            root.right = self.sortedArrayToBST(nums[mid+1:])
        return root







if __name__ == '__main__':
    tree_list_0 = [1,None,2,3,4,None,5,None]
    tree = list_to_tree(tree_list_0)
    tree1_node4 = TreeNode(7)
    tree1_node3 = TreeNode(3)
    tree1_node2 = TreeNode(2)
    tree1_node1 = TreeNode(2)
    tree1_root1 = TreeNode(1,left=tree1_node1,right=tree1_node2)
    solution = Solution()
    # list_tree_1 = solution.preorderTraversal(tree1_root1)
    # print(list_tree_1)
    # list_inorder = solution.inorderTraversal(tree1_root1)
    # print(list_inorder)
    # list_postorder = solution.postorderTravelsal(tree1_root1)
    # list_levelOrder = solution.levelOrder(tree1_root1)
    # deepth = solution.maxDepth(tree1_root1)
    # solution.isValidBST(tree1_root1)
    # solution.isSymmetric(tree1_root1)
    nums = [-10,-3,0,5,9]
    solution.sortedArrayToBST(nums)