# 这类问题通常要求你实现一个给定的类的接口，并可能涉及使用一种或多种数据结构。 这些问题对于提高数据结构是很好的练习。
import math
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
##2.最小栈
    ##设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈

#方法1：用数组实现栈，最小值通过min函数返回，不满足O(1)时间复杂度要求
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = list()
        self.nums = list()


    def push(self, val: int) -> None:
        self.stack.append(val)


    def pop(self) -> None:
        if not self.stack:
            return
        return self.stack.pop()


    def top(self) -> int:
        if not self.stack:
            return
        return self.stack[-1]


    def getMin(self) -> int:
        if not self.stack:
            return
        return min(self.stack)

#方法2：定义节点能够同时存储值和当前情况下最小值
class min_node:
    def __init__(self,val,min=None):
        self.val = val
        self.min = min
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = list()
        self.cur_min = float('inf')

    def push(self, val: int) -> None:
        if self.stack:
            min = self.stack[-1].min
            if val < min:
                node = min_node(val,val)
            else:
                node = min_node(val,min)
        else:
            node = min_node(val,val)
        self.stack.append(node)


    def pop(self) -> None:
        if not self.stack:
            return
        return self.stack.pop().val
    def top(self) -> int:
        if not self.stack:
            return
        return self.stack[-1].val
    def getMin(self) -> int:
        return self.stack[-1].min

##方法3：使用辅助栈存储最小值
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = [math.inf]

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_stack.append(min(self.min_stack[-1],val))


    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()


    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.min_stack[-1]




if __name__ == "__main__":
    nums = [1,2,3,4]
    solution = Shuffle_Array(nums)
    solution.shuffle()
    stack = MinStack()
    stack.push(1)
    stack.push(3)
    stack.push(2)
    min = stack.getMin()




