import pytest
import threading
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


def test_dispose(thread_pool):
    def task():
        time.sleep(0.1)

    thread_pool.enqueue(task)
    time.sleep(0.1)  # give time to complete the task
    thread_pool.dispose()  # The pool should shut down
    assert all(not thread.is_alive() for thread in thread_pool.threads)


def test_multiple_concurrent_tasks(thread_pool):
    result = [0]

    def increment():
        time.sleep(0.1)
        result[0] += 1

    for _ in range(5):
        thread_pool.enqueue(increment)
    time.sleep(0.5)  # give time to complete all tasks
    assert result[0] == 5


def test_pool_size():
    initial_thread_count = threading.active_count()
    pool = ThreadPool(num_threads=5)
    time.sleep(0.1)  # give time for initialization of threads
    assert threading.active_count() == initial_thread_count + 5
    pool.dispose()


def test_pool_size_2():
    num_threads = 5
    initial_thread_count = threading.active_count()
    pool = ThreadPool(num_threads)
    time.sleep(0.1)  # give time for initialization of threads
    new_thread_count = threading.active_count()
    assert new_thread_count - initial_thread_count == num_threads
    pool.dispose()


def test_pool_size_not_less_than_n():
    n = 5
    pool = ThreadPool(num_threads=n)
    time.sleep(0.1)  # give time for initialization of threads
    assert len(pool.threads) == n  # check that there are n threads in the pool
    pool.dispose()

def test_pool_size_not_less_than_n_2():
    n = 5
    pool = ThreadPool(num_threads=n)
    time.sleep(0.1)  # give time for initialization of threads
    assert not(len(pool.threads) < n)  # check that there are not less than n threads in the pool
    pool.dispose()