from random import randint
import time
#第三讲3.1
#二分查找

def find_mid(left,right,method='middle'):
    if method == 'middle':
        return left+int((right-left)*0.5)
    elif method == 'gold':
        return left+int((right-left)*0.618)


def midsearch(nums,target,method='middle'):
    nums.sort()
    left = 0
    right = len(nums)-1
    mid = find_mid(left,right,method)
    while left<=right:
        if target < nums[mid]:
            right = mid - 1
            mid = find_mid(left,right,method)
        elif target > nums[mid]:
            left = mid + 1
            mid = find_mid(left,right,method)
        else:
            return mid
    return -1

if __name__ == '__main__':
    n_nums = 100000
    nums = [ i for i in range(n_nums)]
    target = randint(1,n_nums)
    start_time = time.time()
    middle_res = midsearch(nums,target,method='middle')
    print("%s second"%(time.time()-start_time))
    start_time_2 = time.time()
    middle_res_2 = midsearch(nums, target, method='gold')
    print("%s second" % (time.time() - start_time_2))
    print(middle_res,middle_res_2)
