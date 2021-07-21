class Solution:

    #题目一:合并两个有序列表

    #方法1：冒泡排序
    def merge(self, nums1, m, nums2,n) :
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[i+len(nums1)-n] = (nums2[i])
        for i in range(len(nums1)):
            for j in range(i+1,len(nums1)):
                if nums1[i] > nums1[j]:
                    nums1[i],nums1[j] = nums1[j],nums1[i]
    #方法2：双指针
    def merge(self, nums1, m, nums2,n) :
        result = []
        i,j = 0,0
        while i<m and j<n:
            if nums1[i] < nums2[j]:
                result.append(nums1[i])
                i += 1
            elif nums1[i] > nums2[j]:
                result.append(nums2[j])
                j += 1
            else:
                result.append(nums1[i])
                result.append(nums2[j])
                i += 1
                j += 1
        if i == m and j<n:
            while j != n:
                result.append(nums2[j])
                j += 1
        if j == n and i<m:
            while i != m:
                result.append(nums1[i])
                i += 1
        nums1[:] = result[:]
        #方法3：逆向双指针
        def merge(self, nums1, m, nums2,n) :
            i = m-1
            j = n-1
            index = len(nums1)-1
            while i>=0 and j>=0:
                if nums1[i] >= nums2[j]:
                    nums1[index] = nums1[i]
                    i = i-1
                    index = index-1
                elif nums1[i] < nums2[j]:
                    nums1[index] = nums2[j]
                    j = j-1
                    index = index-1
            if i<0 and j>=0:
                while j>=0:
                    nums1[index] = nums2[j]
                    index = index - 1
                    j = j-1
            return nums1


    #题目2：颜色分类
    #https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xvg25c/
    def sortColors(self,nums):
        if not nums or len(nums)==1:
            return nums
        slow = 0
        while slow<len(nums)-1:
            fast = slow+1
            for i in range(fast,len(nums)):
                if nums[i]<nums[slow]:
                    nums[slow],nums[i] = nums[i],nums[slow]
            slow = slow+1

        return nums

    def sortColors(self,nums):
        zero = 0
        one = 0
        two = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero += 1
            elif nums[i] == 1:
                one += 1
            else:
                two += 1
        for i in range(0,zero):
            nums[i] = 0
        for i in range(zero,zero+one):
            nums[i] = 1
        for i in range(zero+one,zero+one+two):
            nums[i] = 2

        return nums


    def sortColors(self,nums):
        cur = 0
        start = 0
        end = len(nums)-1
        while cur <= end:
            if nums[cur]==0:
                nums[cur],nums[start] = nums[start],nums[cur]
                start += 1
            elif nums[cur]==2:
                nums[cur],nums[end] = nums[end],nums[cur]
                end -= 1
                if nums[cur]!=1:
                    cur -= 1
            cur += 1
        return nums





if __name__ == '__main__':
    solution = Solution()
    nums1 = [2,0,2,1,1,0]
    m,n = 3,3
    nums2 = [2, 5, 6]
    # solution.merge(nums1,m,nums2,n)
    print(solution.sortColors(nums1))
