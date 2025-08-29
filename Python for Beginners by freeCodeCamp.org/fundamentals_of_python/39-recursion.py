# Recursion function. In Python it calls it "self"

# 3! = 3 * 2 * 1 = 6
# 4! = 4 * 3* 2 * 1 = 24
# 5! = 5 * 4 * 3 * 2 * 1 = 120

def factorial(n):
    if n == 1: return 1 # Base Case
    return n * factorial(n-1) # Recursive Case

print(factorial(3))
print(factorial(5))
print(factorial(7))