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
















if __name__ == '__main__':
    math_problem = Math()
    count = math_problem.countPrimes(10)
