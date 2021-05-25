import math
import re


class Math:

    ##1.计数质数
    #统计所有小于非负整数 n 的质数的数量。

    def isPrimes(self,num):
        if num == 0 or num == 1:
            return False
        if num == 2:
            return True
        for i in range(2, num):
            if num % i != 0:
                continue
            return False
        return True

    def isPrimes(self,num):
        if num == 0 or num == 1:
            return False
        if num == 2:
            return True
        if (num-1)%6!=0 and (num+1)%6!=0:
            return False
        for i in range(5, int(math.sqrt(num))+1,6):
            if num % i == 0 or num % (i+2) == 0:
                return False
        return True
    def countPrimes(self, n: int):
        count = 0
        for i in range(n):
            if self.isPrimes(i) == True:
                count = count+1
        return count

    #方法2：埃氏筛
    def countPrimes(self,n):
        if n<2:
            return 0
        elif n<=4:
            return n-2
        isPrimes = n*[1]
        isPrimes[0] = 0
        isPrimes[1] = 0
        count = 0
        for i in range(2,n):
            if isPrimes[i] == 1:
                count = count+1
                for j in range(i*i,n,i):
                    isPrimes[j] = 0
        return count


    def countPrimes(self,n):
        if n<2:
            return 0
        elif n<=4:
            return n-2
        isPrimes = n*[1]
        primes = []
        isPrimes[0] = 0
        isPrimes[1] = 0
        count = 0
        for i in range(2,n):
            if isPrimes[i] == 1:
                count = count+1
                primes.append(i)
            for prime in primes:
                if i*prime<n:
                    isPrimes[i*prime] = 0
                    if i % prime == 0:
                        break
                else: break
        return count

    ##2.3的幂
    #给定一个整数，写一个函数来判断它是否是 3 的幂次方。如果是，返回 true ；否则，返回 false 。
    #方法1：暴力求解
    def isPowerOfThree(self, n: int):
        if n==1:
            return True
        num = 3
        while num<=n:
            if num == n:
                return True
            num = num * 3
        return False
    #方法2：递归求解
    def isPowerOfThree(self, n: int):
        if n == 0:
            return False
        if n == 1:
            return True
        return self.isPowerOfThree(int(n/3)) if (n/3).is_integer() else False
    #方法3：转换为以3为基底的数
    def isPowerOfThree(self, n: int):
        def rebase(value, new_base):
            res = ""
            while value > 0:
                res = str(value % new_base) + res
                value = int(value / new_base)
            return res
        rebase_num = rebase(n,3)
        return re.match(r"^10*",rebase_num).group() == rebase_num if re.match(r"^10*",rebase_num)!= None else False



    #3.罗马数字转换为整数
    def romanToInt(self, s: str) :
        conv_dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
        num = 0
        i = 0
        while i <= len(s)-1:
            if s[i:i+2] in conv_dict:
                num = num + conv_dict[s[i:i+2]]
                i = i+2
            else:
                num = num + conv_dict[s[i]]
                i = i+1
        return num






if __name__ == '__main__':
    math_problem = Math()
    count = math_problem.countPrimes(10)
    is_Three = math_problem.isPowerOfThree(27)
    conv_num = math_problem.romanToInt("MCMXCIV")
    a = 2