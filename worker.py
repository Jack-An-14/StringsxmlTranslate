import threading


class worker(threading.Thread):
    def __init__(self, name, tasks=[]):
        super().__init__()
        self.name = name
        self.tasks = tasks

    def run(self):
        # 判断集合中是否有任务，只要有，就一直执行任务
        while len(self.tasks) > 0:
            job = self.tasks.pop()
            job.start()
            job.join()

