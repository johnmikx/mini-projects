# Every Python file (filename.py) is a module.

from lib import dog

dog.bark()

from lib.dog import bark

bark()

# Other libraries include but no limited to:

# math for math utilities
# re for regular expressions
# json to work with JSON
# datetime to work with dates
# sqlite3 for SQLITE
# os for Operating System utilities
# random for random number generation
# statistics for statistics utilities
# requests to perform HTTP network requests
# http to create HTTP servers
# urllib to manage URLs

import math

print(math.sqrt(4))

from math import sqrt

print(sqrt(4))