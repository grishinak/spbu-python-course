import threading
from typing import Callable, Any, List

class ThreadPool:
    def __init__(self, num_threads: int):
        self.num_threads = num_threads
        self.tasks: List[Callable[[], Any]] = []
        self.lock = threading.Lock()
        self.cond = threading.Condition()
        self.shutdown_event = threading.Event()
        self.threads = []

        for _ in range(num_threads):
            thread = threading.Thread(target=self.worker)
            thread.start()
            self.threads.append(thread)

    def worker(self):
        while not self.shutdown_event.is_set():
            with self.cond:
                while not self.tasks and not self.shutdown_event.is_set():
                    self.cond.wait()  #waiting for a task
                if self.shutdown_event.is_set():
                    break
                task = self.tasks.pop(0)  #taking a task from the queue
            task()  # completing the task

    def enqueue(self, task: Callable[[], Any]):
        with self.lock:
            self.tasks.append(task)
            with self.cond:
                self.cond.notify()  #notifying threads when a task appears

    def dispose(self):
        self.shutdown_event.set()
        with self.cond:
            self.cond.notify_all()  #we release the threads so that they end
        for thread in self.threads:
            thread.join()  #waiting for the threads to finish
