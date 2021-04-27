# 这类问题通常要求你实现一个给定的类的接口，并可能涉及使用一种或多种数据结构。 这些问题对于提高数据结构是很好的练习。
import random
#1.打乱数组
    #方法1：暴力求解，随机采样实现打乱数组
class Shuffle_Array:
    def __init__(self, nums):
        self.nums = nums
    def reset(self):
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums
    def shuffle(self):
        """
        Returns a random shuffling of the array.
        """
        shuffle_nums = self.nums[:]
        sample_nums = self.nums[:]
        length = len(shuffle_nums)
        for i in range(length):
            random_idx = random.randint(0,length-1-i)
            sample_num = sample_nums[random_idx]
            del sample_nums[random_idx]
            shuffle_nums[i] = sample_num
        return shuffle_nums

    #方法2：Fisher-Yates 洗牌算法，交换数组中的元素实现打乱数组
class Shuffle_Array:
    def __init__(self, nums):
        self.nums = nums
    def reset(self):
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums
    def shuffle(self):
        """
        Returns a random shuffling of the array.
        """
        shuffle_nums = self.nums[:]
        for i in range(len(shuffle_nums)):
            idx = random.randrange(i,len(shuffle_nums))
            shuffle_nums[i],shuffle_nums[idx] = shuffle_nums[idx],shuffle_nums[i]
        return shuffle_nums



if __name__ == "__main__":
    nums = [1,2,3,4]
    solution = Shuffle_Array(nums)
    solution.shuffle()




