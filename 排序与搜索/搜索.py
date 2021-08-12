



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

    #题目2：寻找峰值
    #https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xv4hjg/

    #方法1：线性扫描 暴力求解
    def findPeakElement(self, nums):
        if len(nums) == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[len(nums) - 1] > nums[len(nums) - 2]:
            return len(nums) - 1
        for i in range(1, len(nums) - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                return i

    #方法2：递归二分查找
    def findPeakElement(self,nums):

        def search(left,right):
            if left == right:
                return left
            mid = (right+left)//2
            if nums[mid]>nums[mid+1]:
                result =  search(left,mid)
            else:
                result =  search(mid+1,right)
            return result

        return search(0,len(nums)-1)

    #方法3：迭代二分查找
    def findPeakElement(self,nums):
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left+right)//2
            if nums[mid]>nums[mid+1]:
                right = mid
            else:
                left = mid+1
        return left






if __name__ == '__main__':
    solution = Solution()
    nums = [1,2,3,1]
    print(solution.findPeakElement(nums))


