# Threading and multiprocessing can run code in parallel and speed up your
# code.

# Objectives:
# We will learn what is the difference between a process and a thread
# The advantages and disadvantages of process and thread
# How and why are limited by Gil?
# How we can easily use the built-in threading and multiprocessing module to create and run multiple threads or processes

from multiprocessing import Process
import os
import time

def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)

processes = []
num_processes = os.cpu_count()

# create processes
for i in range (num_processes):
    p = Process(target=square_numbers)
    processes.append(p)

# start
for p in processes:
    p.start()

# join
for p in processes:
    p.join()

print('end main')

from threading import Thread

def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)

threads = []
num_threads = 10

# create threads
for i in range (num_threads):
    t = Thread(target=square_numbers)
    threads.append(t)

# start
for t in threads:
    t.start()

# join
for t in threads:
    t.join()

print('end main')