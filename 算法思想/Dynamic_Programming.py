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


    ##问题二：买卖股票的最佳时机
    #方法1：暴力求解
    def maxProfit(self,prices):
        max = 0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                temp = prices[j] - prices[i]
                if temp > max:
                    max = temp
        return max

    #方法2：双指针，动态规划
    def maxProfit(self,prices):
        min = float('inf')
        max = 0
        for i in range(len(prices)):
            if prices[i]<min:
                min = prices[i]
            if prices[i]-min>max:
                max = prices[i]-min
        return max
    #方法3：递归求解（超时）
    def maxProfit(self,prices):
        def help(prices_list):
            if len(prices_list)==1:
                min_p = prices_list[0]
                profit = 0
                return min_p,profit
            n = len(prices_list)
            min_p,profit = help(prices_list[:n-1])
            if prices_list[n-1]<min_p:
                min_p = prices_list[n-1]
            if prices_list[n-1]-min_p>profit:
                profit = prices_list[n-1]-min_p
            return min_p,profit
        min_p,profit = help(prices)
        return profit
        









if __name__ == '__main__':
    dynam_pro = Solution()
    # result = dynam_pro.climbStairs(4)
    prices = [7,1,5,3,6,4]
    result = dynam_pro.maxProfit(prices)
    a=2