
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



















if __name__ == '__main__':
    tree1_node4 = TreeNode(5)
    tree1_node3 = TreeNode(4)
    tree1_node2 = TreeNode(10,left=tree1_node3,right=tree1_node4)
    tree1_node1 = TreeNode(9)
    tree1_root1 = TreeNode(3,left=tree1_node1,right=tree1_node2)
    solution = Solution()
    # list_tree_1 = solution.preorderTraversal(tree1_root1)
    # print(list_tree_1)
    # list_inorder = solution.inorderTraversal(tree1_root1)
    # print(list_inorder)
    # list_postorder = solution.postorderTravelsal(tree1_root1)
    list_levelOrder = solution.levelOrder(tree1_root1)
    deepth = solution.maxDepth(tree1_root1)
    a=2
