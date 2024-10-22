import pytest
import time
from project.threadpool.thread_pool import ThreadPool

@pytest.fixture
def thread_pool():
    pool = ThreadPool(num_threads=3)
    yield pool
    pool.dispose()


def test_enqueue_task(thread_pool):
    result = []

    def task():
        result.append(1)

    thread_pool.enqueue(task)
    time.sleep(0.1)  # give  time to complete the task
    assert result == [1]

def test_multiple_tasks(thread_pool):
    result = []

    def task1():
        result.append(1)

    def task2():
        result.append(2)

    thread_pool.enqueue(task1)
    thread_pool.enqueue(task2)
    time.sleep(0.2)  # give  time to complete the task
    assert result == [1, 2]

def test_pool_size():
    pool = ThreadPool(num_threads=5)
    time.sleep(0.1)  # We give time to initialize the threads
    assert len(pool.threads) == 5
    pool.dispose()

def test_dispose(thread_pool):
    def task():
        time.sleep(0.1)

    thread_pool.enqueue(task)
    time.sleep(0.1)  #give time to complete the task
    thread_pool.dispose()  # The pool should shut down
    assert all(not thread.is_alive() for thread in thread_pool.threads)

def test_multiple_concurrent_tasks(thread_pool):
    result = [0]

    def increment():
        time.sleep(0.1)
        result[0] += 1

    for _ in range(5):
        thread_pool.enqueue(increment)
    time.sleep(0.5)  #give time to complete all tasks
    assert result[0] == 5
