
#栈这种数据结构满足LIFO后进先出的规则，如果想要首先处理最后一个元素那么就可以考虑栈的结构



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


if __name__ == '__main__':
    solution = Solution()
    temp = [73, 74, 75, 71, 69, 72, 76, 73]
    res = solution.dailyTemperatures(temp)
    print(res)
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    res = solution.evalRPN(tokens)
    print(res)