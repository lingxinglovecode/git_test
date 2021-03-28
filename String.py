
# 力扣字符串相关题目 https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnhbqj/

class Solution:

    # 1.反转字符串
    # 编写一个函数，其作用是将输入的字符串反转过来
    def reverseString(self ,string):
        n = len(string)
        for i in range( n//2):
            string[i] ,string[ n - i -1] = string[ n - i -1] ,string[i]

    # 2.整数反转
    # 给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。

    # 方法1：对整数进行操作
    def reverse_int(self ,x):
        num =0  # 记录位数 y=0  #  记  数
        sign = 1
        # 记录符号
        if x<0:
            sign = -1
            x = -x
        # 获取位数
        x_1 = x
        while True:
            if int(x_1/10)!=0:
                num = num+1
                x_1 = int(x_1/10)
            else:
                num = num+1
                break
        # 得到反转后数
        for i in range(num,0,-1):
            y = y+(x%10)* ( 10 **(i - 1))
            x = int(x/10)
        y = sign*y
        if y <-2**31 or y > 2**31-1:
            return 0
        return y

    # 方法2：整数->list->整数
    def reverse_int(self,x):
        sign = 1
        y=0
        if x<0:
            sign =-1
            x=-x
        a = x
        list_x = []
        while a != 0:
            num = a % 10
            list_x.append(num)
            a = int(a/10)
        # self.reverseString(list_x)
        for i in range(len(list_x)):
            y = y+list_x[i] *10**(len( list_x)-i-1)
        y = sign*y
        if y <-2**31 or y >2 **31-1:
            return 0
        return y

    #方法2-改进
    def reverse_int(self ,x):
        y=abs(x)
        num = 0
        boundry = (1<<31)-1 if x>0 else 1<<31
        while y !=0:
            num = y%10 +num*10
            if num>boundry:
                return 0
            y = y//10
        return num if x>0 else -num

    #字符串中的第一个唯一字符
    #给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
    def firstUniqChar(self,s):

        s_list = list(s)
        hashtable = dict()
        for i in s_list:
            if i in hashtable:
                hashtable[i] = hashtable[i] + 1
                continue
            hashtable[i] = 1

        for i in range(len(s_list)):
            if hashtable[s_list[i]] == 1:
                return i
        return -1


        # for key,value in enumerate(hashtable):
        #     if hashtable[value] == 1:
        #         for i in range(len(s_list)):
        #             if s_list[i] == value:
        #                 return i
        # return -1




if __name__=='__main__':
    solution = Solution()
    string = ["H ","a ","n ","n","a","h"]
    x = 1463847412
    s = 'leetcode'
    solution.reverseString(string)

    print(solution.reverse_int(x))
    print(solution.firstUniqChar(s))

