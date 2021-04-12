
#本文主要涵盖与树这一数据结构相关的算法

    #0 树的基本概念与基本操作
    #树是一种包含节点的值和其所有子节点列表的数据结构，在树中最为常见的是二叉树，二叉树之中每一个节点至多包含两个子节点
    #其中两个节点成为左子树和右子树
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

    ## 树的操作基础————遍历

class Solution:
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
            return

        while stack or node:
            while node:
                result.append(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        return result

    #方法3：Morris方法
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


























if __name__ == '__main__':

    tree1_node2 = TreeNode(3)
    tree1_node1 = TreeNode(2,left=tree1_node2)
    tree1_root1 = TreeNode(1,right=tree1_node1)
    solution = Solution()
    list_tree_1 = solution.preorderTraversal(tree1_root1)
    print(list_tree_1)

