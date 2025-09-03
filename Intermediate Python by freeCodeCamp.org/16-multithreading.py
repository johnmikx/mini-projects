# Objectives:

# - We will quickly recap how we can create and start multiple threads
# - We will learn how we can share data between threads and how to use locks to prevent race conditions
# - We will also learn what is daemon process and how we can use a queue for thread safe data exchanges

from threading import Thread, Lock
import time

database_value = 0

def increase(lock):
    global database_value

    with lock:
        local_copy = database_value
        local_copy += 1
        time.sleep(0.1)
        database_value = local_copy

if __name__ == "__main__":

    lock = Lock()
    print('start value', database_value)

    thread1 = Thread(target=increase, args=(lock,))
    thread2 = Thread(target=increase, args=(lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print('end value', database_value)

    print('end main')

# Output:
# start value 0
# end value 2
# end main

from threading import Thread, Lock, current_thread
from queue import Queue
import time

# A queue is a linear data structure that follows the FIFO (First In First
# Out) principle. A good example of a queue is a queue of customers that are
# waiting in line where the customer that came first is also served first.

def worker(q, lock):
    while True:
        value = q.get()
        # processing...
        with lock:
            print(f'in {current_thread().name} got {value}')
        q.task_done()

if __name__ == "__main__":

    q = Queue()
    lock = Lock()
    num_threads = 10

    for i in range(num_threads):
        thread = Thread(target=worker, args=(q, lock))
        thread.daemon=True
        thread.start()

    for i in range(1, 21):
        q.put(i)

    q.join()

    print('end main')