


class Solution:

    # 给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。
    #方法1：使用求和
    def missingNumber(self,nums):
        len_num = len(nums)
        sum = (1+len_num)*len_num/2
        for i in range(len_num):
            sum = sum-nums[i]
        return int(sum)

    #*方法2：位运算
    def missingNumber(self,nums):
        num = 0
        for i in range(len(nums)):
            num = num ^ i ^ nums[i]
        return num ^ len(nums)

if __name__ == '__main__':
    solution = Solution()
    num = solution.missingNumber([3,0,1])
    a = 2