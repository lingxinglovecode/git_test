
#队列，先进先出的数据结构FIFO
import collections
class Solution:

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



if __name__ == '__main__':
    solution = Solution()
    grid = [["1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","0","1","0","1","1"],["0","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","0"],["1","0","1","1","1","0","0","1","1","0","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","0","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","0","1","1","1","1","1","1","0","1","1","1","0","1","1","1","0","1","1","1"],["0","1","1","1","1","1","1","1","1","1","1","1","0","1","1","0","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","1","1"],["1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["0","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","0","1","1","1","1","1","1","1","0","1","1","1","1","1","1"],["1","0","1","1","1","1","1","0","1","1","1","0","1","1","1","1","0","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","0"],["1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","0"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"]]
    num = solution.numIslands(grid)
    print(num)
    a=2








