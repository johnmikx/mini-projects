"""
Objectives:
- We will learn about the concept of context managers and what are they used for
- We will have a look at typical examples of context managers
- How can we implement our own context manager

Context managers are great tool for resource management, they allow you to
allocate and release resources precisely when you want to.

A well-known example is the `with open('filename.nn', 'n')` statement.
"""

# Recommended way to open a file and a typical example on how we can use 
# context managers in order to open a file and allocate the resources
"""
with open('notes.txt', 'w') as file:
    file.write('soe todooo...')
"""

# Traditional way
"""
file = open('notes.txt', 'w')
try:
    file.write('some todoo...')
finally:
    file.close()
"""

# With lock
"""
from threading import Lock
lock = Lock()

lock.acquire()
# ...
lock.release()

with lock:
    # ...
"""

class ManagedFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        print('enter')
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print('exception has been handled')
        # print('exc:', exc_type, exc_value)
        print('exit')
        return True

with ManagedFile('notes.txt') as file:
    print('do some stufff...')
    file.write('some todoo...')
    file.somemethod()
print('continuing')

"""
Output:
enter
do some stufff...
exception has been handled
exit
continuing

"""