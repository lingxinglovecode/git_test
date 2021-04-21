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







if __name__ == '__main__':
    solution = Solution()
    nums1 = [1,2,3,0,0,0]
    m,n = 3,3
    nums2 = [2, 5, 6]
    solution.merge(nums1,m,nums2,n)
