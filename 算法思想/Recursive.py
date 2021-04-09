
#递归的主要实现与例子
#递归的原理以及讲解请看/Users/lianxing/Library/Mobile Documents/iCloud~com~lhy~iMarkdown/Documents/笔记/lianxing/3 工作需求/算法/0.算法思想.md

    #0.递归的主要模板
def recursive(params):
    if params:
        return
    recursive(params)

    #下面是一下常见的递归的例子
class Recursive:
    #1.用递归的思想实现阶乘
    def factorial(self,n):
        if n == 1:
            return 1
        return n * self.factorial(n-1)

    #2.斐波那契数列
    def fibonacci(self,n):
        if n==1 or n==2:
            return 1
        return self.fibonacci(n-1)+self.fibonacci(n-2)

    #3.哈诺塔
    def hanoi(self,n,A,B,C):
        if n ==1 :
            print("从"+A+"移动到"+C)
        else:
            self.hanoi(n-1,A,C,B)
            print("从"+A+"移动到"+C)
            self.hanoi(n-1,B,A,C)




if __name__ == '__main__':
    Recursive = Recursive()
    ##1.阶乘
    result_factorial = Recursive.factorial(3)
    print(result_factorial)
    ##2.斐波那契数列
    result_fibonacci = Recursive.fibonacci(5)
    print(result_fibonacci)
    ##3.哈诺塔
    Recursive.hanoi(4,"A","B","C")







