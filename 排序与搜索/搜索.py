



def isBadVersion(n):
    '''
    测试函数，没有含义
    '''
    return n//2
class Solution:

#题目一：查找第一个错误版本
#n个测试用例中从某一个开始出现错误，这个之后的版本都是错误的，找出第一个出现错误的版本，提供了用于测试是否为错误版本的APIisBadVersion()
    #方法：二分查找
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if isBadVersion(1)==True:
            return 1
        start = 0
        end = n
        while True:
            mid = start+(end-start)//2 if (end-start)%2==0 else start+(end-start)//2+1
            if isBadVersion(mid) == True:
                if isBadVersion(mid-1) == False:
                    return mid
                end = mid
            else:
                start = mid
    #简化版
    def irstBadVersion(self, n):
        left = 1
        right = n
        while left<right:
            mid = (right - left) // 2
            if isBadVersion(mid) == True:
                right = mid
            else:
                left = mid+1
        return left

