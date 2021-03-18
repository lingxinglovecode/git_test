
#
def function(nums):
    if len(nums) == 1:
        return 1
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):

            if (j == len(nums) - 1) and (nums[i] == nums[j]):
                n = i
                return n+1

            if nums[j] == nums[i]:
                continue


            elif nums[j] > nums[i]:
                nums[i+1] = nums[j]
                break
def removeDuplicates(nums) :
    for i in range(len(nums) - 1, 0, -1):
        if nums[i] == nums[i - 1]:
            del nums[i]
    return len(nums)

removeDuplicates(nums)
nums = function(nums)
print(nums)

nums=[-1,-100,3,99]
k=2
def rotate( nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    index = 0
    temp_1 = nums[index]
    l_nums = len(nums)
    index_visted = []
    for i in range(l_nums):
        next_id = (index + k) % l_nums
        if next_id in index_visted:
            index = index + 1
            temp_1 = nums[index]
            next_id = (index + k) % l_nums
        temp_2 = nums[next_id]
        nums[next_id] = temp_1
        temp_1 = temp_2
        index = next_id
        index_visted.append(index)


nums = [1,2,3,4,5,6]
k = 3
rotate(nums,k)


def reverse(nums, start, end):
    for i in range((end - start + 1) // 2):
        nums[i + start], nums[end - i] = nums[end - i], nums[i + start]
    return nums


def rotate(nums, k):
    """
        Do not return anything, modify nums in-place instead.
        """
    reverse(nums, 0, len(nums)-1)
    reverse(nums, 0, k % len(nums)-1)
    reverse(nums, k % len(nums) , len(nums)-1)
nums= [1,2,3,4]
k=2
rotate(nums,k)


def reverse(nums: List[int], start: int, end: int):
    for i in range((end - start + 1) // 2):
        nums[i + start], nums[end - i] = nums[end - i], nums[i + start]
    return nums


class Solution:

    def rotate(self, nums: List[int], k: int) -> None:
        """
            Do not return anything, modify nums in-place instead.
            """
        reverse(nums, 0, len(nums) - 1)
        reverse(nums, 0, k % len(nums) - 1)
        reverse(nums, k % len(nums), len(nums) - 1)
