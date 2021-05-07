

#一些其他可能会遇到的问题

class Solution():

    #方法1：使用api统计字符串中某个字符的个数
    def hammingWeight(self, n: int):
        n = bin(n)
        return n.count('1')

    #方法2：位运算
    def hammingWeight(self,n):
        count = 0
        while n!=0:
            if n&1 == 1:
                count += 1
            n = n>>1
        return count
    #方法3：位运算+查表
    def hammingWeight(self,n):
        table = [0,1,1,2,1,2,2,3,1,2,2,3,2,3,3,4]
        num = 0
        while n!= 0:
            idx = n & 0b1111
            n = n>>4
            num = num + table[idx]
        return num





if __name__ == "__main__":
    solution = Solution()
    num_ones = solution.hammingWeight(0b11111111111111111111111111111101)
    a=2