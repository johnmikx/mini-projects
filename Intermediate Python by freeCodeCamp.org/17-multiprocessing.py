# Objectives:

# - We will go into more detail about the multiprocessing module
# - We will quickly recap how we can create and start multiple processes
# - We will learn how we can share data between processes
# - We will recap how to use locks to prevent race conditions and how to use queues
# - We will learn how to use a process tool to easily manage multiprocesses

from multiprocessing import Process, Value, Array, Lock
import time

def square_numbers():
    for i in range(1000):
        i * i

def add_100(numbers, lock):
    for i in range(100):
        time.sleep(0.01)
        for i in range(len(numbers)):
            with lock:
                numbers[i] +=1

if __name__ == "__main__":

    lock = Lock()
    shared_array = Array('d', [0.0, 100.0, 200.0])
    print('Array at beginning is', shared_array[:])

    p1 = Process(target=add_100, args=(shared_array, lock))
    p2 = Process(target=add_100, args=(shared_array, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('Array at the end is', shared_array[:])

# Output:
# Array at beginning is [0.0, 100.0, 200.0]
# Array at the end is [200.0, 300.0, 400.0]

# A queue can be used for process safe data exchanges.
# A queue is a linear data structure that follows the FIFO principle.

from multiprocessing import Queue

def square(numbers, queue):
    for i in numbers:
        queue.put(i*i)

def make_negative(numbers, queue):
    for i in numbers:
        queue.put(-1*i)

if __name__ == "__main__":

    numbers = range(1, 6)
    q = Queue()

    p1 = Process(target=square, args=(numbers, q))
    p2 = Process(target=make_negative, args=(numbers, q))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    while not q.empty():
        print(q.get())

# A process pool can be used to manage multiple processes. A process pool
# object controls a pool of worker processes to which chops can be submitted.
# And it can manage the available processes for you and split.

# For example, data in smaller chunks, which can then be processed in parallel
# by different processes.

# A pool takes care of a lot of things for you. So you don't have to consider a lot.

from multiprocessing import Pool

def cube(number):
    return number * number * number

if __name__ == "__main__":

    numbers = range(10)
    pool = Pool()

    # map, apply, join, close
    result = pool.map(cube, numbers)
    # pool.apply(cube, numbers[0])

    pool.close()
    pool.join()
    print(result) # [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]