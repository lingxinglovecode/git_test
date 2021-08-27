import multiprocessing
import threading
import time



# def func():
#     print('ran')
#     time.sleep(1)
#     print('done')
#     time.sleep(0.85)
#     print("now down")
#
# x = threading.Thread(target=func,args=())
# x.start()
# print(threading.activeCount())
# time.sleep(0.9)
# print('finally')

#
#
# def count(n):
#     for i in range(1,n+1):
#         print(i)
#         time.sleep(0.01)
# for _ in range(2):
#     x = threading.Thread(target=count,args=(10,))
#     x.start()
# print("done")

class myThread(threading.Thread):
    def __init__(self,threadId, name, count):
        threading.Thread.__init__(self)
        self.name = name
        self.count = count

    def run(self) :
        print("Starting: "+ self.name + '\n')
        threadLock.acquire()
        print_time(self.name,1,self.count)
        threadLock.release()
        print("Exiting: "+ self.name + "\n")

class myThread2(threading.Thread):
    def __init__(self,threadId, name, count):
        threading.Thread.__init__(self)
        self.name = name
        self.count = count

    def run(self) :
        print("Starting: "+ self.name + '\n')
        threadLock.acquire()
        threadLock.release()
        print_time(self.name,1,self.count)
        print("Exiting: "+ self.name + "\n")

def print_time(name, delay, count):
    while count:
        time.sleep(delay)
        print ("%s: %s %s" % (name, time.ctime(time.time()), count) )
        count -= 1
threadLock = threading.Lock()


def multi_thread():
    thread1 = myThread(1, "Thread1", 5)
    thread2 = myThread2(2, "Thread2", 10)
    thread3 = myThread2(3, "Thread3",3)

    thread1.start()
    thread2.start()
    thread3.start()
    thread1.join()
    thread2.join()
    thread3.join()
    print("Done main thread")
multi_thread()

# from multiprocessing import Process
# from time import time, sleep
# def comput_nums(x):
#     print(f"开始计算{x}^10")
#     sleep(3)
#     y = x**5
#     print(f"{x}^10结果是{y}\n")
# def main():
#     start = time()
#     comput_nums(20)
#     comput_nums(30)
#     end = time()
#     print("共用时间：" + str(end-start))
# def multi_process_main():
#     start = time()
#     p1 = Process(target=comput_nums,args=(20,))
#     p2 = Process(target=comput_nums,args=(30,))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     end = time()
#     print("多进程共用时间：" + str(end-start))
#
# if __name__ == '__main__':
#     main()
#     multi_process_main()


# from multiprocessing import Process
# from time import sleep
# counter = 0
# def sub_task(string):
#     global counter
#     while counter < 4:
#         print(string, end='', flush=True)
#         counter += 1
#         sleep(0.1)
#
# def main():
#     Process(target=sub_task, args=('Ping',)).start()
#     Process(target=sub_task, args=('Pong',)).start()
#
# if __name__ == '__main__':
#     main()



# from threading import Thread
# from time import time, sleep
# def comput_nums(x):
#     print(f"开始计算{x}^10")
#     sleep(3)
#     y = x**5
#     print(f"{x}^10结果是{y}\n")
# def main():
#     start = time()
#     comput_nums(20)
#     comput_nums(30)
#     end = time()
#     print("共用时间：" + str(end-start))
# def multi_process_main():
#     start = time()
#     t1 = Thread(target=comput_nums,args=(20,))
#     t2 = Thread(target=comput_nums,args=(30,))
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     end = time()
#     print("多进程共用时间：" + str(end-start))
#
# if __name__ == '__main__':
#     main()
#     multi_process_main()
#



# from threading import Thread
# from time import time, sleep
# class ComputeNums(Thread):
#     def __init__(self,num):
#         super().__init__()
#         self.num = num
#
#     def run(self):
#         print(f"开始计算{self.num}^10")
#         sleep(3)
#         y = self.num ** 5
#         print(f"{self.num}^5结果是{y}\n")
#
# def main():
#     start = time()
#     t1 = ComputeNums(20)
#     t2 = ComputeNums(30)
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     end = time()
#     print("多进程共用时间：" + str(end-start))
# if __name__ == '__main__':
#     main()
#



from time import sleep
from threading import Thread,Lock


class Account(object):

    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money):
        # 先获取锁才能执行后续的代码
        self._lock.acquire()
        try:
            new_balance = self._balance + money
            sleep(0.01)
            self._balance = new_balance
            print(f"账户余额：{self._balance}")
        finally:
            # 在finally中执行释放锁的操作保证正常异常锁都能释放
            self._lock.release()

    @property
    def balance(self):
        return self._balance


class AddMoneyThread(Thread):

    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)


def main():
    account = Account()
    threads = []
    # 创建100个存款的线程向同一个账户中存钱
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    # 等所有存款的线程都执行完毕
    for t in threads:
        t.join()
    print('账户余额为: ￥%d元' % account.balance)


if __name__ == '__main__':
    main()