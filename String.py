
# 力扣字符串相关题目 https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnhbqj/
import re


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

    #3. 字符串中的第一个唯一字符
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

    #4. 有效的字母异位词
    #给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

    #方法一：排序后判断是否相等
    def isAnagram(self,s,t):
        s_list = list(s)
        t_list = list(t)
        s_list.sort()
        t_list.sort()
        if s_list == t_list:
            return True
        return False

    #方法二：利用哈希表判断字符次数
    def isAnagram(self,s,t):
        hashtable = dict()
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] in hashtable:
                hashtable[s[i]] += 1
                continue
            hashtable[s[i]] = 1
        for j in range(len(t)):
            if (t[j] not in hashtable) or (hashtable[t[j]]==0):
                return False
            hashtable[t[j]] -= 1
        return True

    #方法三：利用set集合
    def isAnagram(self,s,t):
        if len(s) != len(t):
            return False
        for i in set(s):
            if s.count(i) != t.count(i):
                return False
        return True

    #5.验证回文串
    #给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。


    #方法1：双指针，开始一个，最后一个，比较字母和数字是否相同，不同则False，若相同当左面指针等于或者大于右面的时候结束
    def isPalindrome(self,s):
        if len(s) <= 1:
            return True
        n = len(s)
        first = 0
        last = n-1
        while True:
            while not s[first].isalnum() and first<n-1:
                first = first + 1
            while not s[last].isalnum() and last>0:
                last = last - 1
            if (not s[first].isalnum()) and (not s[last].isalnum()):
                return True
            if s[first].lower() == s[last].lower():
                first = first + 1
                last = last - 1
                if first >= last:
                    break
                continue
            return False
        return True
    #简化版双指针，思想一样就是简化了一些行
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        left, right = 0, n-1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True



    #方法2：将字符串中所有字符和数字存在另一个变量temp中，判断temp和其倒序字符串temp[::-1]是否相同
    def isPalindrome(self,s):
        temp=''
        for i in range(len(s)):
            if s[i].isalnum():
                temp = temp+s[i]
        if temp == temp[::-1]:
            return True
        return False

    #方法3：使用正则表达式将所有非数字和字母全都替换掉，换成小写后与其倒序字符串比较
    def isPalindrome(self,s):
        temp = re.sub("[^a-zA-Z0-9]","",s)
        temp = temp.lower()
        return temp == temp[::-1]


    #6.请你来实现一个 myAtoi(string s) 函数，使其能将字符串转换成一个 32 位有符号整数
    # 函数myAtoi(string s) 的算法如下：

    # 读入字符串并丢弃无用的前导空格
    # 检查下一个字符（假设还未到字符末尾）为正还是负号，读取该字符（如果有）。 确定最终结果是负数还是正数。 如果两者都不存在，则假定结果为正。
    # 读入下一个字符，直到到达下一个非数字字符或到达输入的结尾。字符串的其余部分将被忽略。
    # 将前面步骤读入的这些数字转换为整数（即，"123" -> 123， "0032" -> 32）。如果没有读入数字，则整数为 0 。必要时更改符号（从步骤 2 开始）。
    # 如果整数数超过 32 位有符号整数范围 [−231, 231 1] ，需要截断这个整数，使其保持在这个范围内。具体来说，小于 −231 的整数应该被固定为 −231 ，大于 231− 1 的整数应该被固定为 231− 1 。
    # 返回整数作为最终结果。
    # 注意：
    #
    # 本题中的空白字符只包括空格字符 ' ' 。
    # 除前导空格或数字后的其余字符串外，请勿忽略 任何其他字符。

    #方法1：根据题意直接编写
    def myAtoi(self, s) :
        i = 0
        num = ''
        sign = 1
        while i <= len(s)-1 and s[i] == " ":
            i = i + 1
        if i > len(s)-1 or s == '':
            return 0
        if s[i] == "-":
            sign = -1
            i = i + 1
        elif s[i] == "+":
            i = i + 1
        boundry = (1<<31)-1 if sign>0 else 1<<31
        while i <= len(s)-1:
            if s[i].isdigit():
                num = num + s[i]
                i = i + 1
                continue
            break
        if num == "":
            return 0
        num = sign * int(num)
        if abs(num) > boundry:
            return sign * boundry
        return num

    #方法2：使用正则表达式
    def myAtoi(self,s):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        s = s.strip()
        num = re.findall('^[\+\-]?\d+',s)
        num = int(*num)
        return max(min(INT_MAX,num),INT_MIN)























if __name__=='__main__':
    solution = Solution()
    string = ["H ","a ","n ","n","a","h"]
    x = 1463847412
    s = 'leetcode'
    t = 'leetcdoe'
    s ="aa, ddw"
    solution.reverseString(string)

    print(solution.reverse_int(x))
    print(solution.firstUniqChar(s))
    print(solution.isAnagram(s,t))
    print(solution.isPalindrome(s))
    print(solution.myAtoi(' '))
