"""
thread_pool.py

A simple thread pool implementation.

This module provides a ThreadPool class that manages a fixed number of threads
to execute tasks concurrently. Tasks are added to the pool and processed by
available threads.

Example usage:

    from project.threadpool.thread_pool import ThreadPool

    def example_task():
        print("Task executed!")

    pool = ThreadPool(num_threads=4)
    pool.enqueue(example_task)
    pool.dispose()
"""

import threading
from typing import Callable, Any, List


class ThreadPool:
    """
    A class that implements a thread pool for executing tasks concurrently.

    Parameters
    ----------
    num_threads : int
        The number of threads to create in the pool.

    Attributes
    ----------
    num_threads : int
        The number of threads in the pool.
    tasks : list of Callable
        The list of tasks to be executed by the threads.
    lock : threading.Lock
        A lock to synchronize access to the tasks list.
    cond : threading.Condition
        A condition variable to notify threads about task availability.
    shutdown_event : threading.Event
        An event to signal threads to terminate.
    threads : list of threading.Thread
        The list of threads in the pool.
    """

    def __init__(self, num_threads: int):
        """
        Initializes the ThreadPool with the specified number of threads.

        Parameters
        ----------
        num_threads : int
            The number of threads to create in the pool.
        """
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
        """
        The worker method that runs in each thread. It waits for tasks to
        become available and executes them until the shutdown event is set.
        """
        while not self.shutdown_event.is_set():
            with self.cond:
                while not self.tasks and not self.shutdown_event.is_set():
                    self.cond.wait()  # Wait for a task to become available
                if self.shutdown_event.is_set():
                    break
                task = self.tasks.pop(0)  # Get the next task from the queue
            task()  # Execute the task

    def enqueue(self, task: Callable[[], Any]):
        """
        Adds a new task to the task queue.

        Parameters
        ----------
        task : Callable[[], Any]
            A callable representing the task to be executed.
        """
        with self.lock:
            self.tasks.append(task)
            with self.cond:
                self.cond.notify()  # Notify one waiting thread

    def dispose(self):
        """
        Signals the threads to terminate and waits for them to finish.

        Already running tasks will not be interrupted.
        """
        self.shutdown_event.set()
        with self.cond:
            self.cond.notify_all()  # Notify all threads to exit
        for thread in self.threads:
            thread.join()  # Wait for all threads to finish
