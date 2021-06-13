
#队列，先进先出的数据结构FIFO
import collections
import copy

import numpy as np

#用栈来实现队列
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = list()


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.queue.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        temp_stack = list()
        while self.queue:
            temp_stack.append(self.queue.pop())
        pop_value = temp_stack.pop()
        while temp_stack:
            self.queue.append(temp_stack.pop())
            return pop_value

    def peek(self) -> int:
        """
        Get the front element.
        """
        temp_stack = list()
        while self.queue:
            temp_stack.append(self.queue.pop())
        pop_value = temp_stack[-1]
        while temp_stack:
            self.queue.append(temp_stack.pop())
        return pop_value


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.queue) == 0




class MyQueue2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = list()
        self.temp_stack = list()
        self.length = 0

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)
        store_stack = list()
        store_stack = self.stack[:]
        self.length = self.length+1
        self.temp_stack = list()
        for i in range(self.length):
            self.temp_stack.append(self.stack.pop())
        self.stack = store_stack

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.length -= 1

        return self.temp_stack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """

        return self.temp_stack[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.length == 0

class MyQueue3:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.in_stack = list()
        self.out_stack = list()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.in_stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.out_stack:
            return self.out_stack.pop()
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.out_stack:
            return self.out_stack[-1]
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.in_stack)+len(self.out_stack) == 0
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()




class Solution:

#问题1：计算网络中的岛屿数量  https://leetcode-cn.com/leetbook/read/queue-stack/kbcqv/
    #方法1：使对队列和广度优先，超时
    def numIslands(self,grid):
        m = len(grid)
        n = len(grid[0])
        used_node = list()
        queue = collections.deque()
        island_num =0

        for i in range(m):
            for j in range(n):
                if (i, j) in used_node:
                    continue
                queue.append((i,j))
                while queue:
                    node = queue.popleft()
                    row,col = node
                    if node not in used_node and grid[row][col] == '1':
                        island_num += 1
                    if grid[row][col] == '1':
                        used_node.append(node)
                        if row-1 >= 0 and grid[row-1][col]=='1':
                            if (row-1,col) not in used_node: queue.append((row-1,col))
                        if row+1 <= m-1 and grid[row+1][col]=='1':
                            if (row+1,col) not in used_node: queue.append((row+1,col))
                        if col-1 >= 0 and grid[row][col-1]=='1':
                            if (row,col-1) not in used_node: queue.append((row,col-1))
                        if col+1 <= n-1 and grid[row][col+1]=='1':
                            if (row,col+1) not in used_node: queue.append((row,col+1))
                        for val in queue:used_node.append(val)
                    elif grid[row][col] == '0':
                        used_node.append(node)
        return island_num

    #方法1优化后
    def numIslands(self,grid):
        m = len(grid)
        n = len(grid[0])
        queue = collections.deque()
        island_num = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='0':
                    continue
                queue.append((i, j))
                island_num += 1
                while queue:
                    node = queue.popleft()
                    row, col = node
                    grid[row][col] = '0'
                    if row - 1 >= 0 and grid[row - 1][col] == '1':
                        queue.append((row - 1, col))
                        grid[row - 1][col] = '0'
                    if row + 1 <= m - 1 and grid[row + 1][col] == '1':
                        queue.append((row + 1, col))
                        grid[row + 1][col] = '0'
                    if col - 1 >= 0 and grid[row][col - 1] == '1':
                        queue.append((row, col - 1))
                        grid[row][col-1] = '0'
                    if col + 1 <= n - 1 and grid[row][col + 1] == '1':
                        queue.append((row, col + 1))
                        grid[row][col+1] = '0'
        return island_num


    ##方法2：DFS深度优先
    def numIslands(self,grid):
        if not grid or len(grid) == 0:
            return
        m = len(grid)
        n = len(grid[0])
        island_num = 0
        def dfs(i,j):
            if (0<=i<m)and(0<=j<n) and grid[i][j] == '1':
                grid[i][j] = '0'
                dfs(i-1,j)
                dfs(i+1,j)
                dfs(i,j+1)
                dfs(i,j-1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    island_num += 1
                    dfs(i,j)
        return island_num


#问题2：打开转盘锁 https://leetcode-cn.com/leetbook/read/queue-stack/kj48j/




    #广度搜索：二叉树的层序遍历
    def openLock(self,deadends,target):
        queue = collections.deque()
        temp_queue = collections.deque()
        queue.append('0000')
        dead_dict = set(deadends)
        level = 0
        def adjust_locknum(num_str):
            res_list = []
            for i in range(len(num_str)):
                num = num_str[i]
                num_adjsted_minus = str(int(num)-1 if int(num)!=0 else 9)
                num_adjsted_plus = str(int(num)+1 if int(num)!=9 else 0)
                res_list.append(num_str[:i]+num_adjsted_minus+num_str[i+1:])
                res_list.append(num_str[:i]+num_adjsted_plus+num_str[i+1:])
            return res_list

        while queue or temp_queue:
            while queue:
                num = queue.popleft()
                if num not in dead_dict:
                    dead_dict.add(num)
                    if num==target:
                        return level
                    lock_nums = adjust_locknum(num)

                    for lock_num in lock_nums:
                        if lock_num not in dead_dict:
                            temp_queue.append(lock_num)
            level = level+1
            queue = temp_queue
            temp_queue = collections.deque()
        return -1

    #算法优化：
    def openLock(self,deadends,target):
        def neighbors(node):
            for i in range(4):
                x = int(node[i])
                for d in (-1, 1):
                    y = (x + d) % 10
                    yield node[:i] + str(y) + node[i + 1:]

        dead = set(deadends)
        queue = collections.deque([('0000', 0)])
        seen = {'0000'}
        while queue:
            node, depth = queue.popleft()
            if node == target: return depth
            if node in dead: continue
            for nei in neighbors(node):
                if nei not in seen:
                    seen.add(nei)
                    queue.append((nei, depth + 1))
        return -1


#问题3：完全平方数 https://leetcode-cn.com/leetbook/read/queue-stack/kfgtt/

    #方法1：广度优先，队列
    def numSquares(self,n):
        queue = collections.deque()
        temp_queue = collections.deque()
        level = 0
        def remain_num(num):
            start = int(np.sqrt(num))
            res_list = [num-x**2 for x in range(start,0,-1)]
            return res_list

        queue.append(n)
        while queue or temp_queue:

            while queue:
                num = queue.popleft()
                if num == 0:
                    return level
                remain_list = remain_num(num)
                temp_queue.extend(remain_list)
            level = level + 1
            queue = temp_queue
            temp_queue = collections.deque()
        return level
    #代码优化，上面解题超时，记录所有访问过的节点
    def numSquares(self,n):
        queue = collections.deque()
        temp_queue = collections.deque()
        num_used = set()
        level = 0
        def remain_num(num):
            start = int(np.sqrt(num))
            res_list = [num-x**2 for x in range(start,0,-1)]
            return res_list

        queue.append(n)
        while queue or temp_queue:
            while queue:
                num = queue.popleft()
                if num == 0:
                    return level
                if num not in num_used:
                    remain_list = remain_num(num)
                    temp_queue.extend(remain_list)
                    num_used.add(num)
            level = level + 1
            queue = temp_queue
            temp_queue = collections.deque()
        return level

    #方法2：动态规划 超时，太多重复运算
    def numSquares(self,n):
        min_num = n
        def issquare(num):
            return np.sqrt(num)%1 == 0

        if issquare(n):
            return 1
        for i in range(1,int(np.sqrt(n))):
            num = self.numSquares(n-i**2) + 1
            min_num = min(num,min_num)
        return min_num

    def numSquares(self,n):
        dp = [0]*(n+1)
        for i in range(1,n+1):
            dp[i] = i
            j = 1
            while j**2 <= i:
                dp[i] = min(dp[i],dp[i-j**2]+1)
                j += 1
        return dp[n]

###问题4：01矩阵 给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。
# https://leetcode-cn.com/leetbook/read/queue-stack/g7pyt/

    # 方法1：广度优先 超时
    def updateMatrix(self, mat):
        res_mat = copy.deepcopy(mat)
        row = len(mat)
        col = len(mat[0])

        dx = [0, 1, -1, 0]
        dy = [1, 0, 0, -1]

        def find_distance(r, c):
            queue = collections.deque()
            temp_queue = collections.deque()
            queue.append((r, c))
            dis = 0
            while queue or temp_queue:
                loc = queue.popleft()
                if mat[loc[0]][loc[1]] == 0:
                    return dis
                for i in range(4):
                    x = loc[0] + dx[i]
                    y = loc[1] + dy[i]
                    if x >= 0 and x < row and y >= 0 and y < col:
                        temp_queue.append((x, y))
                if not queue:
                    queue = temp_queue
                    temp_queue = collections.deque()
                    dis += 1

        for i in range(row):
            for j in range(col):
                dis = find_distance(i, j)
                res_mat[i][j] = dis
        return res_mat

    # 方法1改进：遍历0进行更新 还是超时了 比第一害差
    def updateMatrix(self, mat):
        res_mat = copy.deepcopy(mat)
        for i in range(len(res_mat)):
            for j in range(len(res_mat[0])):
                res_mat[i][j] = float('inf')
        row = len(mat)
        col = len(mat[0])
        res_dict = dict()
        dx = [0, 1, -1, 0]
        dy = [1, 0, 0, -1]

        def updata(r, c):
            temp_dict = dict()
            queue = collections.deque()
            temp_queue = collections.deque()
            queue.append((r, c))
            dis = 0
            while queue or temp_queue:
                loc = queue.popleft()
                if loc not in temp_dict:
                    if dis < res_mat[loc[0]][loc[1]]:
                        res_mat[loc[0]][loc[1]] = dis
                    temp_dict[loc] = 1

                    for i in range(4):
                        x = loc[0] + dx[i]
                        y = loc[1] + dy[i]
                        if x >= 0 and x < row and y >= 0 and y < col and ((x, y) not in temp_dict):
                            temp_queue.append((x, y))
                if not queue:
                    queue = temp_queue
                    dis += 1
                    temp_queue = collections.deque()

        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    updata(i, j)
        return res_mat

    # 方法1改进2 一次遍历所有0：
    # 参考官方题解：https://leetcode-cn.com/problems/01-matrix/solution/01ju-zhen-by-leetcode-solution/
    def updateMatrix(self, mat):
        queue = collections.deque()
        row = len(mat)
        col = len(mat[0])
        res_mat = [[0] * col for _ in range(row)]
        zeros = [(i, j) for i in range(row) for j in range(col) if mat[i][j] == 0]
        res_dic = set(zeros)
        queue.extend(zeros)

        while queue:
            loc = queue.popleft()
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                x = loc[0] + dx
                y = loc[1] + dy
                if x >= 0 and x < row and y >= 0 and y < col and ((x, y) not in res_dic):
                    res_mat[x][y] = res_mat[loc[0]][loc[1]] + 1
                    queue.append((x, y))
                    res_dic.add((x, y))
        return res_mat

    def updateMatrix(self, mat):
        row = len(mat)
        col = len(mat[0])
        dp = [[float('inf')] * col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    dp[i][j] = 0

        for i in range(row):
            for j in range(col):
                if i - 1 >= 0:
                    dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j])
                if j - 1 >= 0:
                    dp[i][j] = min(dp[i][j - 1] + 1, dp[i][j])

        for m in range(row - 1, -1, -1):
            for n in range(col - 1, -1, -1):
                if m + 1 < row:
                    dp[m][n] = min(dp[m + 1][n] + 1, dp[m][n])
                if n + 1 < col:
                    dp[m][n] = min(dp[m][n + 1] + 1, dp[m][n])
        return dp



if __name__ == '__main__':
    solution = Solution()
    grid = [["1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","0","1","0","1","1"],["0","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","0"],["1","0","1","1","1","0","0","1","1","0","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","0","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","0","1","1","1","1","1","1","0","1","1","1","0","1","1","1","0","1","1","1"],["0","1","1","1","1","1","1","1","1","1","1","1","0","1","1","0","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","1","1"],["1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["0","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","0","1","1","1","1","1","1","1","0","1","1","1","1","1","1"],["1","0","1","1","1","1","1","0","1","1","1","0","1","1","1","1","0","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","0"],["1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","0"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"]]
    num = solution.numIslands(grid)
    print(num)
    a=2
    deadends = ["5557","5553","5575","5535","5755","5355","7555","3555","6655","6455","4655","4455","5665","5445","5645","5465","5566","5544","5564","5546","6565","4545","6545","4565","5656","5454","5654","5456","6556","4554","4556","6554"]
    target = "5555"

    print(solution.openLock(deadends,target))

    num_s = solution.numSquares(10)
    print(num_s)

    # Your MyQueue object will be instantiated and called as such:
    obj = MyQueue2()
    x = 10
    y = 20
    obj.push(x)
    obj.push(y)
    param_2 = obj.pop()
    param_3 = obj.peek()
    param_4 = obj.empty()

    ##问题4：
    mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    res = solution.updateMatrix(mat)
    print(res)







