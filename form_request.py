import threading
import time
import collections
from producer import Producer

queue_size = 10
number_consumers = 3

queue = collections.deque(maxlen=queue_size)
mutex = threading.Lock()
condition = threading.Condition(mutex)





