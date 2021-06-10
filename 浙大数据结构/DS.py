#本节主要记录浙大数据结构课程中出现的编程题目，题目均可在在PTA中找到
#PTA https://pintia.cn/problem-sets?tab=0
#浙大版《数据结构（第2版）》题目集


class Solution:




    def get_input(self,fuc="max_subsequence"):
        if fuc == "max_subsequence":
            k = int(input())
            nums = [int(num) for num in input().split()]
            return k,nums

# 实例1.1 最大子序和
# https://pintia.cn/problem-sets/434/problems/5404
    # 方法1：直接遍历求解
    def max_subsequence(self,k,nums):
        '''
        input:
        k: 输入数据个数 e.g. 4
        nums:输入的列表 e.g.[1,3,4,3]
        return: 最大子序和
        '''
        max_sum = 0
        for i in range(k):
            temp_sum = 0
            for j in range(i,k):
                temp_sum = temp_sum + nums[j]
                if temp_sum > max_sum:
                    max_sum = temp_sum
        return max_sum

    #方法2：分而治之
    def max_subsequence(self,k,nums):
        start = 0
        end = k-1
        def help(start,end):
            mid = int((end+start)/2)

            if start == end:
                return nums[start] if nums[start]>0 else 0

            left_max = help(start,mid)
            right_max = help(mid+1,end)


            left_sum = 0
            left_sum_max = 0
            for i in range(mid,start-1,-1):
                left_sum = left_sum+nums[i]
                if left_sum>left_sum_max:
                    left_sum_max = left_sum
            right_sum = 0
            right_sum_max = 0
            for j in range(mid+1,end+1,1):
                right_sum = right_sum+nums[j]
                if right_sum>right_sum_max:
                    right_sum_max=right_sum
            mid_max = left_sum_max+right_sum_max


            return max(left_max,right_max,mid_max)


        max_sum = help(start,end)
        return max_sum

    #方法3：贪心算法
    def max_subsequence(self,k,nums):
        temp = 0
        max_res = 0
        for i in range(k):
            temp = temp + nums[i]
            if temp > max_res:
                max_res = temp
            elif temp < 0:
                temp = 0
        return max_res






if __name__ == '__main__':
    solution = Solution()
    get_input = False
    if get_input:
        k,nums = solution.get_input('max_subsequence')
    k = 6
    nums = [-2,11,-4,13,-5,-2]
    print(solution.max_subsequence(k,nums))




