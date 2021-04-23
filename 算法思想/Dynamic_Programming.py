'''
本节主要介绍动态规划相关算法题
'''

class Solution:


    #问题一：爬楼梯
    #假设你正在爬楼梯。需要 n 阶你才能到达楼顶。每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
    #注意：给定 n 是一个正整数。
    #方法1.0：递归
    def climbStairs(self, n: int):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        return self.climbStairs(n-1)+self.climbStairs(n-2)

    #方法1.1：优化后递归 具有记忆功能的递归
    #对递归结果进行存储避免重复运算
    def climbStairs(self , n):
        # nonlocal a_list
        a_list = n*[0]
        def help(n):
            if n<=2:
                return n
            if a_list[n-2]!=0 and a_list[n-3]!=0:
                return a_list[n-2]+a_list[n-3]
        for i in range(n):
            a_list[i] = help(i+1)
        return a_list[n-1]
    #方法2：动态规划
    #再找到递归公式后进行简化，只用两个变量存储之前两个状态即可
    def climbStairs(self, n):
        q = 0
        r = 1
        for i in range(n):
            p = q
            q = r
            r = p+q
        return r
    #方法3:公式计算
    #直接用斐波那契数列的公式
    def climbStairs(self, n):
        import math
        sqrt_5 = math.sqrt(5)
        return int(1/sqrt_5*(((1+sqrt_5)/2)**(n+1)-((1-sqrt_5)/2)**(n+1)))









if __name__ == '__main__':
    dynam_pro = Solution()
    result = dynam_pro.climbStairs(4)
    a=2