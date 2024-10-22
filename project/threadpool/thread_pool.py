import threading
from typing import Callable, Any

class ThreadPool:
    def __init__(self, num_threads: int):
        self.num_threads = num_threads
        self.tasks = []
        self.lock = threading.Lock()
        self.task_available = threading.Event()
        self.threads = []
        self.shutdown_event = threading.Event()
        
        for _ in range(num_threads):
            thread = threading.Thread(target=self.worker)
            thread.start()
            self.threads.append(thread)

    def worker(self):
        while not self.shutdown_event.is_set():
            self.task_available.wait()  # Ожидание появления задачи
            with self.lock:
                if not self.tasks:
                    self.task_available.clear()  # Если нет задач, возвращаемся в ожидание
                    continue
                task = self.tasks.pop(0)  # Берем задачу из очереди
            task()  # Выполняем задачу

    def enqueue(self, task: Callable[[], Any]):
        with self.lock:
            self.tasks.append(task)
            self.task_available.set()  # Уведомляем потоки о появлении задачи

    def dispose(self):
        self.shutdown_event.set()
        self.task_available.set()  # Освобождаем потоки, чтобы они завершились
        for thread in self.threads:
            thread.join()  # Ждем завершения потоков
