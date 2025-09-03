# Python comes with different built-in modules to generate random numbers.
# we will have a look at the `random` module for pseudorandom numbers,
# the `secrets` module for cryptographically strong random numbers, and the
# NumPy random module to generate arrays with random numbers.

# `import random` used to generate pseudorandom numbers for various distributions.
# It's called pseudorandom because the numbers seem random, but they are reproducible.
# We will see how we can reproduce the data.

import random

# Inclusive lower and upper bound
a = random.random() # random float in range from 0 <= x <= 1
print(a)

# Inclusive lower and upper bound
a = random.uniform(1, 10) # random float in range from 1 <= x <= 10
print(a)

a = random.randint(1, 10) # random integer in range from 1 <= x <= 10
print(a)

# Inclusive lower bound and Exclusive upper bpund
a = random.randrange(1, 10) # random integer in range from 1 <= x < 10
print(a)

# random.normalvariate(mu, sigma)
# mean(mu) = 0 | sigma(std) = 1
a = random.normalvariate(0, 1)
print(a)

mylist = list('ABCDEFGH')
a = random.choice(mylist)
print(a)

mylist = list('ABCDEFGH')
a = random.choices(mylist, k=3)
print(a)

mylist = list('ABCDEFGH')
a = random.sample(mylist, 3)
print(a)

mylist = list('ABCDEFGH')
random.shuffle(mylist)
print(mylist)

random.seed(1)
print(random.random())
print(random.randint(1, 10))
random.seed(2)
print(random.random())
print(random.randint(1, 10))

random.seed(1)
print(random.random())
print(random.randint(1, 10))

random.seed(2)
print(random.random())
print(random.randint(1, 10))

import secrets
# `secrets` module has only three functions. And they should be used for
# things like passwords, security tokens, or account authentication things.
# For all these purposes, you should use the `secrets` module. The disadvantage
# is that it takes more times for these algorithms, but they will generate a true
# random number.

a = secrets.randbelow(10)
print(a)

a = secrets.randbits(4) # produces 4 binary values like 1111 or 15 as max
print(a)

mylist = list('ABCDEFGH')
a = secrets.choice(mylist)
print(a)

import numpy as np

a = np.random.rand(3)
print(a) # [....., ....., .....]

a = np.random.rand(3, 4)
print(a)

a = np.random.rand(3, 4, 5)
print(a)

# np.random.randint(included, excluded, (size))
a = np.random.randint(0, 10) # a number
print(a)

a = np.random.randint(0, 10, 3) # 1 x 3 array
print(a)

a = np.random.randint(0, 10, (3, 4)) # 3 x 4 array
print(a)

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
print(arr)
np.random.shuffle(arr)
print(arr)

np.random.seed(1)
print(np.random.rand(3, 3))
np.random.seed(1)
print(np.random.rand(3, 3))