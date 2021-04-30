import math

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
    def isPowerOfThree(self, n: int):
        if n==1:
            return True
        num = 3
        while num<=n:
            if num == n:
                return True
            num = num * 3
        return False

    def isPowerOfThree(self, n: int):
        if n == 0:
            return False
        if n == 1 or n == 3:
            return True
        return self.isPowerOfThree(int(n/3)) if (n/3).is_integer() else False


















if __name__ == '__main__':
    math_problem = Math()
    count = math_problem.countPrimes(10)
    is_Three = math_problem.isPowerOfThree(0)
    a = 2