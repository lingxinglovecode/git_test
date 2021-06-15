import collections
#栈这种数据结构满足LIFO后进先出的规则，如果想要首先处理最后一个元素那么就可以考虑栈的结构
import copy


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


#用队列实现栈

#方法1：用一个队列暂存元素
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = collections.deque()
        self.temp_queue = collections.deque()


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.append(x)


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        length = len(self.queue)
        while length-1:
            self.temp_queue.append(self.queue.popleft())
            length = length-1
        res = self.queue.popleft()
        self.queue = self.temp_queue
        return res


    def top(self) -> int:
        """
        Get the top element.
        """
        length = len(self.queue)
        while length - 1:
            self.temp_queue.append(self.queue.popleft())
            length = length - 1
        res = self.queue[0]
        self.temp_queue.append(self.queue.popleft())
        self.queue = self.temp_queue
        return res


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue) == 0

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = collections.deque()


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.append(x)
        for i in range(0,len(self.queue)-1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue.popleft()


    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue[0]


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue) == 0




class Solution:


    #########问题1：每日温度##########
    #https://leetcode-cn.com/leetbook/read/queue-stack/genw3/
    #请根据每日 气温 列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不会升高，请在该位置用 0 来代替。

    #方法1：两个循环，超时
    def dailyTemperatures(self,temperatures):
        day_num = len(temperatures)
        temp_list = [0]*day_num
        for i in range(day_num-1,0,-1):
            temp = temperatures.pop()
            for j in range(len(temperatures)):
                if temperatures[j]<temp:
                    temp_list[j] = i-j
        return temp_list
    def dailyTemperatures1(self,temperatures):
        result = [0]*len(temperatures)
        for i in range(len(temperatures)):
            for j in range(i+1,len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    result[i] = j-i
                    break
        return result
    #方法2：栈
    def dailyTemperatures(self,temperatures):
        stack = list()
        result = [0]*len(temperatures)
        stack.append(0)
        i = 1
        while i<len(temperatures):
            temp = stack[-1]
            if temperatures[i] > temperatures[temp]:
                result[temp] = i-temp
                stack.pop()
                if stack:
                    continue
                stack.append(i)
            else:
                stack.append(i)
            i = i+1
        return result
    #简化版本
    def dailyTemperatures(self,temperatures):
        stack = list()
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and (temperatures[i] >temperatures[stack[-1]]):
                idx = stack.pop()
                result[idx] = i - idx
            stack.append(i)
        return result

    #方法3：KMP？
    def dailyTemperatures(self,temperatures):
        result = [0]*len(temperatures)
        for i in range(len(temperatures)-2,-1,-1):
            j = i+1
            while j<len(temperatures):
                if temperatures[i] < temperatures[j]:
                    result[i] = j-i
                    break
                elif result[j] == 0:
                    result[i] = 0
                    break
                else:
                    j = j + result[j]
        return result

    #############题目2：逆波兰表达式求值################
    #https://leetcode-cn.com/leetbook/read/queue-stack/gomvm/

    def evalRPN(self, tokens):
        stack = list()
        cal_dict = {"+","-","*","/"}
        def calculate(sign,num1,num2):
            if sign == "+":
                return num1+num2
            elif sign == "*":
                return num1*num2
            elif sign == "/":
                return int(num1/num2)
            elif sign == "-":
                return num1-num2
        for i in range(len(tokens)):
            if tokens[i] not in cal_dict:
                stack.append(int(tokens[i]))
            else:
                num_2 = stack.pop()
                num_1 = stack.pop()
                result = calculate(tokens[i],num_1,num_2)
                stack.append(result)
        return stack[0]

    #######题目3：克隆图########
    #https://leetcode-cn.com/leetbook/read/queue-stack/gmcr6/
    #给定一个无向连通图中的一个节点的引用，返回改图的深拷贝

    #方法1：递归隐性栈+深度优先算法
    def cloneGraph(self,node):
        visited = dict()
        def help(node):
            if node == None:
                return
            if node.val in visited:
                return visited[node.val]
            new_node = Node(val=node.val)
            visited[node.val] = new_node
            new_node.neighbors = [help(neighbor) for neighbor in node.neighbors]
            return new_node
        new_node = help(node)

        return new_node

    #方法2：队列+广度优先算法
    def cloneGraph(self,node):
        if node == None:
            return
        queue = collections.deque()
        queue.append(node)
        node_dict = dict()
        start_node = Node(val=node.val)
        node_dict[node.val] = start_node
        while queue:
            cur = queue.popleft()
            for neighbor in cur.neighbors:
                if neighbor.val in node_dict:
                    node_dict[cur.val].neighbors.append(node_dict[neighbor.val])
                else:
                    new_node = Node(neighbor.val)
                    node_dict[cur.val].neighbors.append(new_node)
                    node_dict[neighbor.val] = new_node
                    queue.append(neighbor)
        return start_node




    #########题目4：目标和#########
    #https://leetcode-cn.com/leetbook/read/queue-stack/ga4o2/

    #解法1：递归
    def findTargetSumWays(self, nums, target):
        if len(nums)==1 and abs(nums[0]) == abs(target):
            if nums[0]==0:
                return 2
            return 1
        elif len(nums) == 1 and abs(nums[0])!=abs(target):
            return 0
        length = len(nums)
        last = nums[length-1]
        return self.findTargetSumWays(nums[:length-1],target-last)+self.findTargetSumWays(nums[:length-1],target+last)

    def findTargetSumWays(self,nums,target):
        count = 0
        def backtarck(nums,target,index,sum):
            nonlocal count
            if index == len(nums):
                if sum == target:
                    count = count+1
            else:
                backtarck(nums,target,index+1,sum-nums[index])
                backtarck(nums,target,index+1,sum+nums[index])
            return count
        res = backtarck(nums,target,0,0)
        return res

    def findTargetSumWays(self, nums, target):
        def dfs(i,t):
            if i == len(nums):
                return 1 if t==0 else 0
            return dfs(i+1,t-nums[i]) + dfs(i+1,t+nums[i])
        return dfs(0,target)

    ##解法2：动态规划
    def findTargetSumWays(self,nums,target):
        n = len(nums)
        neg = (sum(nums)-target)/2
        if neg<0 or neg != int(neg):
            return 0
        neg = int(neg)
        dp = [[0 for i in range(neg+1)]for j in range(n+1)]
        dp[0][0] = 1
        for i in range(1,n+1):
            num = nums[i-1]
            for j in range(neg+1):
                if num > j:
                    dp[i][j] = dp[i-1][j]
                elif num <= j:
                    dp[i][j] = dp[i-1][j-num] + dp[i-1][j]
        return dp[n][neg]

    def findTargetSumWays(self, nums, S) :
        sumAll = sum(nums)
        if S > sumAll or (S + sumAll) % 2:
            return 0
        target = (S + sumAll) // 2

        dp = [0] * (target + 1)
        dp[0] = 1

        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] + dp[j - num]
        return dp[-1]

    #########题目5：字符串解码#########
    #https://leetcode-cn.com/leetbook/read/queue-stack/gdwjv/
    def decodeString(self,s):
        stack = list()
        s_len = len(s)
        i = 0
        while i<s_len:
            stack.append(s[i])
            if stack[-1] == ']':
                stack.pop()
                temp=''
                alpha = stack.pop()
                while  alpha!= '[':
                    temp = temp + alpha
                    alpha = stack.pop()
                temp = temp[::-1]
                num = ''
                while len(stack) and stack[-1].isdigit():
                    num = num + stack.pop()
                temp = int(num[::-1]) * temp
                stack.extend(list(temp))
            i = i+1
        res = ''.join(stack)
        return res

    ###问题6：图像渲染
    #https://leetcode-cn.com/leetbook/read/queue-stack/g02cj/

    #方法1：广度优先算法+队列
    def floodFill(self,image,sr,sc,newColor):
        len_row = len(image)
        len_col = len(image[0])
        memory_dict = dict()
        queue = collections.deque()
        original_color = image[sr][sc]
        def find_neighbour(sr,sc):
            neighbors = []
            if sr>0 and image[sr-1][sc]==original_color:
                up = (sr-1,sc)
                neighbors.append(up)
            if sr<len_row-1 and image[sr+1][sc]==original_color:
                down = (sr+1,sc)
                neighbors.append(down)
            if sc>0 and image[sr][sc-1]==original_color:
                left = (sr,sc-1)
                neighbors.append(left)
            if sc<len_col-1 and image[sr][sc+1]==original_color:
                right = (sr,sc+1)
                neighbors.append(right)
            return neighbors
        queue.append((sr,sc))
        image[sr][sc] = newColor
        while queue:
            loc = queue.popleft()
            neighbors = find_neighbour(loc[0],loc[1])
            for neighbor in neighbors:
                if neighbor not in memory_dict:
                    image[neighbor[0]][neighbor[1]] = newColor
                    memory_dict[neighbor] = 1
                    queue.append(neighbor)
        return image

    #修改一下找邻居节点的方式
    def floodFill(self,image,sr,sc,newColor):
        len_row = len(image)
        len_col = len(image[0])
        memory_dict = dict()
        queue = collections.deque()
        original_color = image[sr][sc]
        def find_neighbour( sr, sc):
            dx = [1, 0, 0, -1]
            dy = [0, 1, -1, 0]
            neighbors = list()
            for i in range(4):
                x = sr + dx[i]
                y = sc + dy[i]
                if (x >= 0 and x < len_row) and (y >= 0 and y < len_col) and image[x][y]==original_color:
                    neighbors.append((x,y))
            return neighbors

        queue.append((sr,sc))
        image[sr][sc] = newColor
        while queue:
            loc = queue.popleft()
            neighbors = find_neighbour(loc[0],loc[1])
            for neighbor in neighbors:
                if neighbor not in memory_dict:
                    image[neighbor[0]][neighbor[1]] = newColor
                    memory_dict[neighbor] = 1
                    queue.append(neighbor)
        return image





    # 方法2：深度优先+栈
    def floodFill(self, image, sr, sc, newColor):
        len_row = len(image)
        len_col = len(image[0])
        memory_dict = dict()
        original_color = image[sr][sc]

        def dfs(row, col):
            if image[row][col] != original_color or (row, col) in memory_dict:
                return
            image[row][col] = newColor
            memory_dict[(row, col)] = 1
            if row > 0:
                dfs(row - 1, col)
            if row < len_row - 1:
                dfs(row + 1, col)
            if col > 0:
                dfs(row, col - 1)
            if col < len_col - 1:
                dfs(row, col + 1)

        dfs(sr, sc)
        return image






    ####问题7：钥匙与房间
    #https://leetcode-cn.com/leetbook/read/queue-stack/gle1r/

    #解法1：深度优先算法
    def canVisitAllRooms(self, rooms) :
        visited = set()
        stack = list()
        stack.extend(rooms[0])
        visited.add(0)
        while stack:
            next_room = stack.pop()
            if next_room not in visited:
                visited.add(next_room)
                stack.extend(rooms[next_room])
        return len(visited) == len(rooms)

    #解法2：广度优先算法
    def canVisitAllRooms(self,rooms):
        visited =  set()
        queue = collections.deque()
        queue.extend(rooms[0])
        visited.add(0)
        while queue:
            next_room = queue.popleft()
            if next_room not in visited:
                queue.extend(rooms[next_room])
                visited.add(next_room)
        return len(visited) == len(rooms)

    #解法3：递归
    def canVisitAllRooms(self,rooms):
        visited = set()
        def dfs(room_num):
            if room_num in visited:
                return
            visited.add(room_num)
            for room in rooms[room_num]:
                dfs(room)
        dfs(0)
        return len(visited) == len(rooms)





if __name__ == '__main__':
    solution = Solution()
    # temp = [73, 74, 75, 71, 69, 72, 76, 73]
    # res = solution.dailyTemperatures(temp)
    # print(res)
    # tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    # res = solution.evalRPN(tokens)
    # print(res)
    # node_1 = Node(1)
    # node_2 = Node(2)
    # node_1.neighbors.append(node_2)
    # node_2.neighbors.append(node_1)
    # new_node =solution.cloneGraph(node_1)
    # print(node_1)
    # nums = [1,1,1,1,1,0]
    # target = 3
    # ways = solution.findTargetSumWays(nums,target)
    # print(ways)

    # Your MyStack object will be instantiated and called as such:
    # obj = MyStack()
    # x = 7
    # y=9
    # obj.push(x)
    # obj.push(y)
    # param_2 = obj.pop()
    # param_3 = obj.top()
    # param_4 = obj.empty()

    # s = "2[a2[wlx]bc]3[cd]ef"
    # res=solution.decodeString(s)
    # print(res)

    # image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    # sr = 1
    # sc = 1
    # newColor = 2
    # img = solution.floodFill(image,sr,sc,newColor)
    # print(img)

    rooms = [[2,3],[],[2],[1,3,1]]
    vis = solution.canVisitAllRooms(rooms)
    print(vis)

