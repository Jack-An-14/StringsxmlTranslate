import queue
import string
import threading
import worker


class threadPool:
    """
        自定义线程池

        成员变量
            1、任务队列
            2、当前线程数量
            3、核心线程数量
            4、最大线程数量
            5、任务队列的长度

        成员方法
            1、提交任务
            2、执行任务
    """
    tasks = []
    threadnum = 0

    def __init__(self, coresize, maxsize, worksize):
        self.coresize = coresize
        self.maxsize = maxsize
        self.worksize = worksize

    def submit(self, thread=threading.Thread):
        if len(self.tasks) >= self.worksize:
            print("任务" + thread.name + "丢弃")
        else:
            self.tasks.append(thread)
            self.execthread(thread)

    def execthread(self, thread):
        if self.threadnum < self.coresize:
            item = worker.worker("核心线程" + str(self.threadnum), self.tasks)
            item.start()
            item.join()
            self.threadnum += 1
        elif self.threadnum < self.maxsize:
            item = worker.worker("非核心线程" + str(self.threadnum), self.tasks)
            item.start()
            item.join()
            self.threadnum += 1
        else:
            print("被缓存")



