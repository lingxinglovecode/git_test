import collections
#栈这种数据结构满足LIFO后进先出的规则，如果想要首先处理最后一个元素那么就可以考虑栈的结构

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

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


if __name__ == '__main__':
    solution = Solution()
    temp = [73, 74, 75, 71, 69, 72, 76, 73]
    res = solution.dailyTemperatures(temp)
    print(res)
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    res = solution.evalRPN(tokens)
    print(res)
    node_1 = Node(1)
    node_2 = Node(2)
    node_1.neighbors.append(node_2)
    node_2.neighbors.append(node_1)
    new_node =solution.cloneGraph(node_1)
    print(node_1)
    nums = [1,1,1,1,1,0]
    target = 3
    ways = solution.findTargetSumWays(nums,target)
    print(ways)