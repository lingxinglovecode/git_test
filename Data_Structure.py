import collections
#队列 Queue
#FIFO 先进先出的数据结构
class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0]*k
        self.head_idx = 0
        self.count = 0
        self.capacity = k


    def enQueue(self, value: int) -> bool:
        if self.count == self.capacity:
            return False
        tail_idx = (self.head_idx+self.count) % self.capacity
        self.queue[tail_idx] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.count == 0:
            return False
        self.head_idx = (self.head_idx+1) % self.capacity
        self.count -= 1
        return True


    def Front(self) -> int:
        if self.count == 0:
            return -1
        return self.queue[self.head_idx]


    def Rear(self) -> int:
        if self.count == 0:
            return -1
        return self.queue[(self.head_idx+self.count-1)%self.capacity]

    def isEmpty(self) -> bool:
        if self.count == 0:
            return True
        return False


    def isFull(self) -> bool:
        return self.count == self.capacity

##python标准库中内置的实现队列的函数collection.deque

if __name__ == '__main__':
    test_queue = MyCircularQueue(4)
    test_queue.enQueue(2)


    test_queue_1 = collections.deque([1,2,3,4])
    test_queue_1.popleft() #从开头弹出元素
    print(test_queue_1)




