import collections


class Solution:

    #1.删除数组中的重复项
    def removeDuplicates(self,nums) :
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] == nums[i - 1]:
                del nums[i]
        return len(nums)

    #2.买卖股票的最佳时机

    def maxProfit(self, prices) :
        sum = 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                money=prices[i+1] - prices[i]
                sum = sum+money
            else:
                continue
        return sum

    #3.旋转数组
    #方法一
    def rotate( self,nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        temp_1 = nums[index]
        l_nums = len(nums)
        index_visted = []
        for i in range(l_nums):
            next_id = (index + k) % l_nums
            if next_id in index_visted: #如果下一个位置已经被访问过
                index = index + 1
                temp_1 = nums[index]
                next_id = (index + k) % l_nums
            temp_2 = nums[next_id]
            nums[next_id] = temp_1
            temp_1 = temp_2
            index = next_id
            index_visted.append(index)
    #方法二
    def reverse(self,nums, start, end):
        for i in range((end - start + 1) // 2):
            nums[i + start], nums[end - i] = nums[end - i], nums[i + start]
        return nums


    def rotate(self,nums, k):
        """
            Do not return anything, modify nums in-place instead.
            """
        self.reverse(nums, 0, len(nums)-1)
        self.reverse(nums, 0, k % len(nums)-1)
        self.reverse(nums, k % len(nums) , len(nums)-1)
    #方法三
    def rotate(self,nums,k):
        list_nums  = nums.copy()
        for i in range(len(nums)):
            list_nums[(i+k)%len(nums)] = nums[i]
        nums[:] = list_nums[:]




    #4.重复元素检查
    def containsDuplicate(nums):
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False


    #5.给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
    def singleNumber(self,nums):
        nums.sort()
        if nums[0] != nums[1]:
            return nums[0]
        if nums[len(nums)-1] != nums[len(nums) - 2]:
            return nums[len(nums)-1]
        for i in range(1,len(nums)-1):
            if (nums[i]!=nums[i-1]) and (nums[i]!=nums[i+1]):
                return nums[i]

    def singleNumber(self,nums):
        result = 0
        for i in range(len(nums)):
            result = result^nums[i]
        return result

    #6.给定两个数组，编写一个函数来计算它们的交集。输出结果中每个元素出现的次数，应与元素在两个数组中出现次数的最小值一致。
    # 我们可以不考虑输出结果的顺序。
    def intersect(self,nums1,nums2):
        nums1.sort()
        nums2.sort()
        stop = 0
        i, j = 0, 0
        inter = []
        while not ((i == len(nums1)) or (j == len(nums2))):
            if nums1[i] == nums2[j]:
                inter.append(nums1[i])
                i = i + 1
                j = j + 1
            elif nums1[i] > nums2[j]:
                j = j + 1
            elif nums1[i] < nums2[j]:
                i = i + 1
        return inter

    def intersect(self,nums1,nums2):
        if len(nums1)<len(nums2):
            return self.intersect(nums2,nums1)

        m = collections.Counter()
        inter = []
        for num in nums1:
            m[num] = m[num] +1
        for num in nums2:
            if (num in m) and (m[num]!=0):
                inter.append(num)
                m[num] = m[num]-1
        return inter

#7.给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
    def plusOne(self,digits):
        num = 0
        for i in range(len(digits)):
            num = num+digits[i] * 10**(len(digits)-i-1)
        num_plus = num+1
        result = []
        while num_plus >0:
            i =num_plus%10
            result.append(i)
            num_plus =  num_plus // 10
        result.reverse()
        return result

    def plusOne(self,digits):
        for i in range(len(digits) - 1, -1, -1):
            digits[i] = digits[i] + 1
            if digits[i] != 10:
                return digits
            digits[i] = 0
        digits = [0] * (len(digits) + 1)
        digits[0] = 1
        return digits
#8.给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

    #我的解法：双指针
    def moveZeroes(self,nums):
        i=0
        while i<len(nums)-1:

            if nums[i]!=0:
                i = i+1
                continue
            j = i
            while j!=len(nums)-1:
                if nums[j] != 0:
                    break
                j = j+1
            nums[i],nums[j] = nums[j],nums[i]
            i = i+1
        return nums
    #网友的解法：双指针
    def moveZeroes(self,nums):
        fast = 0
        slow = 0
        while fast<len(nums):
            if nums[fast]!=0:
                nums[fast],nums[slow] = nums[slow],nums[fast]
                slow = slow + 1
            fast = fast + 1
        return nums


#9.给定一个整数数组 num和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
# 你可以按任意顺序返回答案。

    #1.暴力解法
    def twoSum(self,nums,target):
        result = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    result.append(i)
                    result.append(j)
                    return result

    #2.使用哈希表
    def twoSum(self,nums,target):
        hashtable = dict()
        for i in range(len(nums)):
            if (target - nums[i]) in hashtable:
                return [hashtable[target-nums[i]],i]
            hashtable[nums[i]] = i

#10.有效的数独，判断一个9x9的数独是否有效

    ##本来想分别循环行列和方块的，这样子就要写三个循环非常麻烦,写了一个行检测的就放弃了
    def row_test(row):
        hashtable = dict()
        for i in range(1,10,1):
            hashtable[i] = 0
        for num in range(len(row)):
            if row[num].isalnum():
                if hashtable[int(row[num])] == 1:
                    return False
                hashtable[int(row[num])] = 1
        return True

    #方法：哈希表，一次遍历
    def isValidSudoku(self,board):
        row = [{} for i in range(9)]
        col = [{} for i in range(9)]
        block = [{} for i in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                else:
                    num = int(board[i][j])
                    block_idx = (i//3)*3 +j//3
                    block[block_idx][num] = block[block_idx].get(num,0)+1
                    row[i][num] = row[i].get(num,0)+1
                    col[j][num] = col[j].get(num,0)+1
                    if block[block_idx][num]>1 or row[i][num]>1 or col[j][num]>1:
                        return False
        return True

    #11.旋转一个nxn的二维矩阵，顺时针旋转90°

    #方法一：先上下颠倒然后沿着对角线交换元素
    def rotate(self, matrix) :
        n = len(matrix)
        # 上下颠倒
        for row in range(n // 2):
            for col in range(n):
                matrix[row][col], matrix[n - row - 1][col] = matrix[n - row - 1][col], matrix[row][col]
        # 沿着对角线互换元素
        for row in range(n):
            for col in range(row):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        return matrix

    #方法二：
    def rotate(self, matrix) :
        n = len(matrix)
        for layer in range(n//2):
            for num in range(layer,n-layer-1):
                temp = matrix[num][n-layer-1]
                matrix[num][n-layer-1] = matrix[layer][num]
                temp,matrix[n-layer-1][n-num-1] = matrix[n-layer-1][n-num-1],temp
                temp,matrix[n-num-1][layer] = matrix[n-num-1][layer],temp
                matrix[layer][num] = temp
        return matrix

    #12.三数之和
    #列表中找到三个数使其和为0
    #https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xvpj16/

    #解法一：暴力三重循环 哈希表去重 超时
    def threeSum(self,nums):
        nums.sort()
        res = []
        seen = set()
        for i in range(len(nums)):
            if nums[i]>0:
                break

            for j in range(i+1,len(nums)):

                if nums[i]+nums[j]>0:
                    break
                for k in range(len(nums)-1,j,-1):
                    if nums[i]+nums[j]+nums[k]<0:
                        break
                    if nums[i]+nums[j]+nums[k] == 0:
                        if (nums[i],nums[j],nums[k]) not in seen:
                            res.append([nums[i],nums[j],nums[k]])
                            seen.add((nums[i],nums[j],nums[k]))

        return res

    #解法二：一重循环+双指针
    def threeSum(self,nums):
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i==0 or nums[i]!=nums[i-1]:
                start = i+1
                end = len(nums)-1
                while start < end:
                    if start>i+1 and nums[start] == nums[start-1]:
                        start = start+1
                        continue
                    if end<len(nums)-1 and nums[end] == nums[end+1]:
                        end = end-1
                        continue
                    if nums[i]+nums[start]+nums[end]>0:
                        end = end-1
                    elif nums[i]+nums[start]+nums[end]<0:
                        start = start+1
                    elif nums[i]+nums[start]+nums[end]==0:
                        res.append([nums[i],nums[start],nums[end]])
                        start = start+1
                        end = end-1
        return res



    #13.矩阵归零
    #https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xvmy42/

    #内存消耗m*n
    def setZeroes(self, matrix) :
        row = len(matrix)
        col = len(matrix[0])
        memory = []
        def help(x,y):
            for i in range(row):
                matrix[i][y] = 0
            for j in range(col):
                matrix[x][j] = 0


        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    memory.append((i,j))
        for x,y in memory:
            help(x,y)
    #内存消耗m+n
    def setZeroes(self,matrix):
        row = len(matrix)
        col = len(matrix[0])
        memory_row = [1]*row
        memory_col = [1]*col

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    memory_col[j] = 0
                    memory_row[i] = 0

        for i in range(len(memory_row)):
            if memory_row[i] == 0:
                for col_idx in range(col):
                    matrix[i][col_idx] = 0
        for j in range(len(memory_col)):
            if memory_col[j] == 0:
                for row_idx in range(row):
                    matrix[row_idx][j] = 0
    #好吧瞎搞内存消耗还是m*n
    def setZeroes(self,matrix):
        memory = ""
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    memory = memory+str(i)+"/"+str(j)+"/"
        idx = 0
        flag = 0
        while idx<len(memory):
            start = idx
            bound = idx
            while memory[bound] != '/':
                bound =  bound+1
            memory_num = int(memory[start:bound])
            idx = bound+1
            if flag == 0:
                for col_idx in range(col):
                    matrix[memory_num][col_idx] = 0
                flag = 1
            else:
                for row_idx in range(row):
                    matrix[row_idx][memory_num] = 0
                flag = 0

    def setZeroes(self,matrix):
        row = len(matrix)
        col = len(matrix[0])
        flag_first_row = 0
        flag_first_col = 0
        for j in range(col):
            if matrix[0][j] == 0:
                flag_first_row = 1
                break
        for i in range(row):
            if matrix[i][0] == 0:
                flag_first_col = 1
                break
        for i in range(1,row):
            for j in range(1,col):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # for m in range(1,col):
        #     if matrix[0][m] == 0:
        #         for row_idx in range(row):
        #             matrix[row_idx][m] = 0
        #
        # for n in range(1,row):
        #     if matrix[n][0] == 0:
        #         for col_idx in range(col):
        #             matrix[n][col_idx] = 0

        #上面两个循环简化一下：
        for n in range(1,row):
            for m in range(1,col):
                if matrix[n][0]==0 or matrix[0][m]==0:
                    matrix[n][m] = 0


        if flag_first_col == 1:
            for j in range(col):
                matrix[j][0] = 0

        if flag_first_row == 1:
            for i in range(row):
                matrix[0][i] = 0


    #14.字母异位词分组
    #https://leetcode-cn.com/problems/group-anagrams/solution/zi-mu-yi-wei-ci-fen-zu-by-leetcode-solut-gyoc/

    #方法1：哈希表
    def  groupAnagrams(self, strs) :
        hash_dict = dict()
        idx = 0
        res = []
        for i in range(len(strs)):
            list_s = list(strs[i])
            list_s.sort()
            sort_str = "".join(list_s)
            if sort_str not in hash_dict:
                hash_dict[sort_str] = idx
                res.append([strs[i]])
                idx = idx + 1
            else:
                idx = hash_dict[sort_str]
                res[idx].append(strs[i])

        return res

    #方法1简化，哈希表值中直接存储列表
    def  groupAnagrams(self, strs) :
        hash_dict = collections.defaultdict(list)
        for st in strs:
            key = "".join(sorted(st))
            hash_dict[key].append(st)
        return list(hash_dict.values())



















if __name__=='__main__':
    # nums1 = [0]
    # nums2 = [1,2,3,4]
    solution = Solution()
    # solution.intersect(nums1,nums2)
    # solution.moveZeroes(nums1)
    # solution.singleNumber(nums)
    # matrix = [[1, 2], [3, 4]]
    # matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    # matrix=solution.rotate(matrix)
    # print(matrix)

    #12.
    # nums = [0,0,0,0]
    # res = solution.threeSum(nums)
    # print(res)

    #13.
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    solution.setZeroes(matrix)
    a = 2



