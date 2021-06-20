#本节主要记录浙大数据结构课程中出现的编程题目，题目均可在在PTA中找到
#PTA https://pintia.cn/problem-sets?tab=0
#浙大版《数据结构（第2版）》题目集

class Polynomial:
    def __init__(self,coefficient=0,power=0,next=None):
        self.coe = coefficient
        self.power = power
        self.next = next



class Solution:
    def __init__(self,fuc="max_subsequence"):
        self.fuc = fuc

    def get_input(self):
        if self.fuc == "max_subsequence":
            k = int(input())
            nums = [int(num) for num in input().split()]
            return k, nums
        if self.fuc == 'multiple_sum':
            y1 = [int(num) for num in input().split()]
            y2 = [int(num) for num in input().split()]
        return y1[0], y1[1:], y2[0], y2[1:]

    def output(self,**kwargs):
        if self.fuc == "multiple_sum":
            sum_result = kwargs['sum_result']
            mul_result = kwargs['mul_result']
            sum_result_list = []
            mul_result_list = []
            while sum_result:
                sum_result_list.append(sum_result.coe)
                sum_result_list.append(sum_result.power)
                sum_result = sum_result.next
            while mul_result:
                mul_result_list.append(mul_result.coe)
                mul_result_list.append(mul_result.power)
                mul_result = mul_result.next
            print(' '.join(map(str, mul_result_list)))
            print(' '.join(map(str, sum_result_list)))


# 编程题1-复杂度1 最大子序列和问题
# https://pintia.cn/problem-sets/1399202744970727424/problems/1399203880238600192
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

#编程题1-复杂度2： 最大子序列和问题
# https://pintia.cn/problem-sets/1399202744970727424/problems/1399203880238600193
#要求返回子序列的第一个和最后一个元素
    def max_subsequence_2(self,k,nums):
        temp = 0
        max_res = 0
        temp_start = 0
        res_start = 0
        res_end = 0
        flag = 1
        for i in range(k):
            temp = temp + nums[i]
            if flag:
                temp_start = i
                flag = 0
            if temp > max_res:
                max_res = temp
                res_start = temp_start
                res_end = i
            elif temp < 0:
                temp = 0
                flag = 1
        if max(nums) < 0:
            res_start = 0
            res_end = len(nums) - 1
        elif max(nums) == 0:
            for i in range(k):
                if nums[i] == 0:
                    res_start = i
                    res_end = i
                    break
        return max_res, nums[res_start], nums[res_end]

#编程题2 一元多项式的乘法与加法运算
    def multiple_sum(self,y1_num,y1,y2_num,y2):
        '''
        y1: [3 4 -5 2] 3x^4-5x^2
        y2: [3 4 -5 2] 3x^4-5x^2
        '''
        def construct(num,y):
            if num==0:
                return Polynomial()
            for i in range(num):
                if i == 0:
                    y_list = Polynomial()
                    y_list.coe = y[0]
                    y_list.power = y[1]
                    node = y_list
                else:
                    new_node = Polynomial()
                    new_node.coe = y[i*2]
                    new_node.power = y[i*2+1]
                    node.next = new_node
                    node = new_node
            return y_list

        def polynomial_sum(y1_list,y2_list):
            result = Polynomial()
            pointer_1 = y1_list
            pointer_2 = y2_list
            if (pointer_1.coe==0 and pointer_1.power==0) or (pointer_2.coe==0 and pointer_2.power==0):
                return pointer_1 if pointer_2.coe==0 else pointer_2
            node = result
            while pointer_1 and pointer_2 :
                power_1 = pointer_1.power
                power_2 = pointer_2.power
                if power_1<power_2:
                    new_node = Polynomial()
                    new_node.coe = pointer_2.coe
                    new_node.power = pointer_2.power
                    node.next = new_node
                    node = new_node
                    pointer_2 = pointer_2.next
                elif power_1 > power_2:
                    new_node = Polynomial()
                    new_node.coe = pointer_1.coe
                    new_node.power = pointer_1.power
                    node.next = new_node
                    node = new_node
                    pointer_1 = pointer_1.next
                elif power_1 == power_2:
                    new_node = Polynomial()
                    new_node.coe = pointer_1.coe + pointer_2.coe
                    if new_node.coe == 0:
                        pointer_1 = pointer_1.next
                        pointer_2 = pointer_2.next
                        continue
                    new_node.power = pointer_1.power
                    node.next = new_node
                    node = new_node

                    pointer_1 = pointer_1.next
                    pointer_2 = pointer_2.next
            while pointer_1:
                new_node = Polynomial()
                new_node.coe = pointer_1.coe
                new_node.power = pointer_1.power
                node.next = new_node
                node = new_node
                pointer_1 = pointer_1.next
            while pointer_2:
                new_node = Polynomial()
                new_node.coe = pointer_2.coe
                new_node.power = pointer_2.power
                node.next = new_node
                node = new_node
                pointer_2 = pointer_2.next

            return result.next


        def polynomial_mul(y1_list,y2_list):
            pointer_1 = y1_list
            res = Polynomial()
            while pointer_1:
                y1_coe = pointer_1.coe
                y1_power = pointer_1.power
                pointer_2 = y2_list
                temp_res = Polynomial()
                head_flag = 1
                while pointer_2:
                    y2_coe = pointer_2.coe
                    y2_power = pointer_2.power
                    if head_flag:
                        temp_res.coe = y1_coe*y2_coe
                        temp_res.power = y1_power+y2_power
                        node = temp_res
                        head_flag = 0
                    else:
                        new_node = Polynomial()
                        new_node.coe = y1_coe * y2_coe
                        new_node.power = y1_power + y2_power
                        node.next = new_node
                        node = new_node
                    pointer_2 = pointer_2.next
                res = polynomial_sum(res,temp_res)
                pointer_1 = pointer_1.next
            return res

        y1_list = construct(y1_num, y1)
        y2_list = construct(y2_num, y2)
        sum_result = polynomial_sum(y1_list, y2_list)
        if sum_result == None:
            sum_result = Polynomial()
        mul_result = polynomial_mul(y1_list,y2_list)
        return sum_result,mul_result


if __name__ == '__main__':
    # solution = Solution()
    # get_input = False
    # if get_input:
    #     k,nums = solution.get_input('max_subsequence')
    # k = 6
    # nums = [-10,1,2,3,4,-5,-6,-3,4,3]
    # print(solution.max_subsequence_2(k,nums))

    ##编程题2 一元多项式的乘法与加法运算
    solution = Solution('multiple_sum')
    sum_result,mul_result = solution.multiple_sum(0,[0,0],1,[-3,4])
    solution.output(sum_result=sum_result,mul_result=mul_result)
    a =2



