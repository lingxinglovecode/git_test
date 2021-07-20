#本节是关于回溯算法的题目
#h回溯的方法会探索所有的可能性并返回
import copy
import numpy as np
class Solution:

    # 回溯算法的框架
    # result = []
    # def backtarck(路径，选择列表):
    #     if 满足结束条件：
    #         result.add(路径)
    #         return
    #     for 选择 in 选择列表：
    #         做选择
    #         backtrack(路径，选择列表)
    #         撤销选择

    #1.全排列问题
    #给定终止数，返回从1-终止数的所有全排列可能
    def full_arrange(self,num):
        num_list = list(range(num+1))[1:]
        result = []
        path = []
        def backtarck(path,choice):
            if len(choice) == 0:
                result.append(copy.deepcopy(path))
                return
            for i in range(len(choice)) :
                path.append(choice[i])
                choice[0],choice[i] = choice[i],choice[0]
                backtarck(path,choice[1:])
                path.pop()
        backtarck(path,num_list)
        return result


    def permute(self,nums):
        result = []
        def backtarck(cur,choose_list):
            if len(choose_list) == 0:
                result.append(copy.deepcopy(cur))
                return
            for i in range(len(choose_list)):
                cur.append(choose_list[i])
                choose_list[i],choose_list[0] = choose_list[0],choose_list[i]
                backtarck(cur,choose_list[1:])
                choose_list[i], choose_list[0] = choose_list[0], choose_list[i]
                cur.pop()
        backtarck([],nums)
        return result








    #2.电话号码的字母组合
    #https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xv8ka1/
    def letterCombinations(self, digits) :
        if not digits:
            return []
        digit_dict = {1:"",2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        if int(digits) in digit_dict:
            return list(digit_dict[int(digits)])
        comb = self.letterCombinations(digits[1:])
        list_res = []
        for a in list(digit_dict[int(digits[0])]):
            for b in list(comb):
                list_res.append(a+b)
        return list_res
    #套用回溯模板求解
    def letterCombinations(self,digits):
        if not digits:
            return []
        digit_dict = {1: "", 2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
        result = []
        def backtarck(path,choices):
            if len(choices) == 0:
                result.append(copy.deepcopy(path))
                return
            for way in choices[0]:
                path = path+way
                backtarck(path,choices[1:])
                path = path[:-1]
        choices = []
        for num in digits:
            if int(num)>1:
                choices.append(digit_dict[int(num)])
        path = ""
        backtarck(path,choices)
        return result

    #3.括号生成
    #模板写法
    def generateParenthesis1(self, n) :
        result = []
        res_set = set()
        def backtarck(path,choices):
            if len(choices) == 0:
                if path not in res_set:
                    result.append((path))
                    res_set.add(path)
                return
            for i in range(len(choices)):
                path = path+choices[i]

                if path.count(')')>path.count('('):
                    path = path[:-1]
                    continue
                if i>0 and choices[i] == choices[0]:
                    path = path[:-1]
                    continue
                if path.count('(') <= n:
                    choices[i],choices[0] = choices[0],choices[i]
                    backtarck(path,choices[1:])
                    path = path[:-1]
        path = ''
        choices = ''
        for i in range(n):
            choices = choices + '()'
        choices = list(choices)
        backtarck(path,choices)
        return result

    #模板优化写法
    def generateParenthesis(self,n):
        result = []

        def backtarck(S,left,right):
            if len(S) == 2*n:
                result.append(S)
                return
            if left<n:
                S = S+'('
                backtarck(S,left+1,right)
                S = S[:-1]
            if right<left:
                S = S + ')'
                backtarck(S,left,right+1)
                S = S[:-1]
        backtarck('',0,0)
        return result


    #4.子集 返回数组中所有可能的子集
    #https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xv67o6/
    def subsets(self,nums):
        result = []
        res_set = set()
        def backtarck(cur,choose_list):

            if str(set(sorted(cur))) not in res_set:
                result.append(copy.deepcopy(cur))
                res_set.add(str(set(sorted(cur))))
            else:
                return
            for i in range(len(choose_list)):
                cur.append(choose_list[i])
                choose_list[i],choose_list[0] = choose_list[0],choose_list[i]
                backtarck(cur,choose_list[1:])
                choose_list[i], choose_list[0] = choose_list[0], choose_list[i]
                cur.pop()
        backtarck([],nums)
        return result


    def subsets(self,nums):
        result = []
        def backtarck(cur,choose_list):
            result.append(copy.deepcopy(cur))
            if len(choose_list)==0:
                return
            for i in range(len(choose_list)):
                cur.append(choose_list[i])
                backtarck(cur,choose_list[i+1:])
                cur.pop()
        backtarck([],nums)
        return result

    ##方法2：循环方法
    def subsets(self,nums):
        result = [[]]
        temp =  copy.deepcopy(result)
        for i in range(len(nums)):
            for ele in temp:
                ele.append(nums[i])
                result.append(copy.deepcopy(ele))
            temp =  copy.deepcopy(result)
        return result

    ##方法3：二进制排序子集
    def subsets(self,nums):
        n = len(nums)
        binary_mask = []
        for i in range(2**n):
            binary_mask.append(bin(i)[2:].zfill(n))
#本节是关于回溯算法的题目
#h回溯的方法会探索所有的可能性并返回
import copy
class Solution:

    # 回溯算法的框架
    # result = []
    # def backtarck(路径，选择列表):
    #     if 满足结束条件：
    #         result.add(路径)
    #         return
    #     for 选择 in 选择列表：
    #         做选择
    #         backtrack(路径，选择列表)
    #         撤销选择

    #1.全排列问题
    #给定终止数，返回从1-终止数的所有全排列可能
    def full_arrange(self,num):
        num_list = list(range(num+1))[1:]
        result = []
        path = []
        def backtarck(path,choice):
            if len(choice) == 0:
                result.append(copy.deepcopy(path))
                return
            for i in range(len(choice)) :
                path.append(choice[i])
                choice[0],choice[i] = choice[i],choice[0]
                backtarck(path,choice[1:])
                path.pop()
        backtarck(path,num_list)
        return result


    def permute(self,nums):
        result = []
        def backtarck(cur,choose_list):
            if len(choose_list) == 0:
                result.append(copy.deepcopy(cur))
                return
            for i in range(len(choose_list)):
                cur.append(choose_list[i])
                choose_list[i],choose_list[0] = choose_list[0],choose_list[i]
                backtarck(cur,choose_list[1:])
                choose_list[i], choose_list[0] = choose_list[0], choose_list[i]
                cur.pop()
        backtarck([],nums)
        return result








    #2.电话号码的字母组合
    #https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xv8ka1/
    def letterCombinations(self, digits) :
        if not digits:
            return []
        digit_dict = {1:"",2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        if int(digits) in digit_dict:
            return list(digit_dict[int(digits)])
        comb = self.letterCombinations(digits[1:])
        list_res = []
        for a in list(digit_dict[int(digits[0])]):
            for b in list(comb):
                list_res.append(a+b)
        return list_res
    #套用回溯模板求解
    def letterCombinations(self,digits):
        if not digits:
            return []
        digit_dict = {1: "", 2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
        result = []
        def backtarck(path,choices):
            if len(choices) == 0:
                result.append(copy.deepcopy(path))
                return
            for way in choices[0]:
                path = path+way
                backtarck(path,choices[1:])
                path = path[:-1]
        choices = []
        for num in digits:
            if int(num)>1:
                choices.append(digit_dict[int(num)])
        path = ""
        backtarck(path,choices)
        return result

    #3.括号生成
    #模板写法
    def generateParenthesis1(self, n) :
        result = []
        res_set = set()
        def backtarck(path,choices):
            if len(choices) == 0:
                if path not in res_set:
                    result.append((path))
                    res_set.add(path)
                return
            for i in range(len(choices)):
                path = path+choices[i]

                if path.count(')')>path.count('('):
                    path = path[:-1]
                    continue
                if i>0 and choices[i] == choices[0]:
                    path = path[:-1]
                    continue
                if path.count('(') <= n:
                    choices[i],choices[0] = choices[0],choices[i]
                    backtarck(path,choices[1:])
                    path = path[:-1]
        path = ''
        choices = ''
        for i in range(n):
            choices = choices + '()'
        choices = list(choices)
        backtarck(path,choices)
        return result

    #模板优化写法
    def generateParenthesis(self,n):
        result = []

        def backtarck(S,left,right):
            if len(S) == 2*n:
                result.append(S)
                return
            if left<n:
                S = S+'('
                backtarck(S,left+1,right)
                S = S[:-1]
            if right<left:
                S = S + ')'
                backtarck(S,left,right+1)
                S = S[:-1]
        backtarck('',0,0)
        return result


    #4.子集 返回数组中所有可能的子集
    #https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xv67o6/
    def subsets(self,nums):
        result = []
        res_set = set()
        def backtarck(cur,choose_list):

            if str(set(sorted(cur))) not in res_set:
                result.append(copy.deepcopy(cur))
                res_set.add(str(set(sorted(cur))))
            else:
                return
            for i in range(len(choose_list)):
                cur.append(choose_list[i])
                choose_list[i],choose_list[0] = choose_list[0],choose_list[i]
                backtarck(cur,choose_list[1:])
                choose_list[i], choose_list[0] = choose_list[0], choose_list[i]
                cur.pop()
        backtarck([],nums)
        return result

    #方法1：回溯 优化后
    def subsets(self,nums):
        result = []
        def backtarck(cur,choose_list):
            result.append(copy.deepcopy(cur))
            if len(choose_list)==0:
                return
            for i in range(len(choose_list)):
                cur.append(choose_list[i])
                backtarck(cur,choose_list[i+1:])
                cur.pop()
        backtarck([],nums)
        return result

    ##方法2：循环方法
    def subsets(self,nums):
        result = [[]]
        temp =  copy.deepcopy(result)
        for i in range(len(nums)):
            for ele in temp:
                ele.append(nums[i])
                result.append(copy.deepcopy(ele))
            temp =  copy.deepcopy(result)
        return result

    ##方法3：二进制排序子集
    def subsets(self,nums):
        n = len(nums)
        binary_mask = []
        result = []
        for i in range(2**n):
            binary_mask.append(bin(i)[2:].zfill(n))
        for mask in binary_mask:
            temp = []
            for i in range(n):
                if mask[i] == '1':
                    temp.append(nums[i])
            result.append(temp)
        return result


    #5.单词搜索 在一个矩阵中搜索是否含有固定词语

    #回溯思想
    def exist(self,board,word):
        flag = np.ones_like(board)
        row = len(board)
        col = len(board[0])
        def backtrack(index,flag,word_index):
            flag[index] = '0'
            if word_index == len(word):
                return True

            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                x = index[0] + dx
                y = index[1] + dy
                if x >= 0 and x < row and y >= 0 and y < col and flag[x][y]!='0' and board[x][y] == word[word_index]:
                    if backtrack((x,y), copy.deepcopy(flag), word_index + 1):
                        return True
            return False

        board = np.array(board)
        for i in range(len(word)):
            if word[i] not in board:
                return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if backtrack((i,j),copy.deepcopy(flag),1):
                        return True
        return False



    #回溯简化
    def exist(self,board,word):
        visited = set()
        def check(i,j,k):
            if board[i][j] != word[k]:
                return False
            if k == len(word)-1:
                return True
            visited.add((i,j))
            result = False
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_x = dx+i
                new_y = dy+j
                if new_x>=0 and new_x<len(board) and new_y>=0 and new_y<len(board[0]) and (new_x,new_y) not in visited:
                    if check(new_x,new_y,k+1):
                        result = True
                        break
            visited.remove((i,j))
            return result

        for i in range(len(board)):
            for j in range(len(board[0])):
                if check(i,j,0):
                    return True
        return False



    #再次简化，使用#表示已经搜索过的区域
    def exist(self,board,word):

        def check(i,j,k):
            if board[i][j] != word[k]:
                return False
            if k == len(word)-1:
                return True
            flag = False
            temp = board[i][j]
            board[i][j] = '#'
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_x = i+dx
                new_y = j+dy
                if new_x>=0 and  new_x<len(board) and new_y>=0 and new_y<len(board[0]) and board[new_x][new_y]!='#':
                    if check(new_x,new_y,k+1):
                        flag = True
                        break
            board[i][j] = temp
            return flag


        for i in range(len(board)):
            for j in range(len(board[0])):
                if check(i,j,0):
                    return True
        return False




























if __name__ == '__main__':
    solution = Solution()
    # solution.letterCombinations("123")
    # solution.full_arrange(3)
    solution.generateParenthesis1(4)
    solution.generateParenthesis(4)
    solution.subsets([1,2,3])

    board =[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "SEE"
    print(solution.exist(board,word))





