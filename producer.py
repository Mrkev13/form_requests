import threading

class Producer(threading.Thread):
    def __init__(self, queue, condition, queue_size):
        super().__init__()
        self.queue = queue
        self.condition = condition
        self.queue_size = queue_size

    