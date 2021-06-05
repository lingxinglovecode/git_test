
#队列，先进先出的数据结构FIFO
import collections
import numpy as np
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







