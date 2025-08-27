a = 5      # 0b0101
b = 3      # 0b0011

and_result = a & b      # performs binary AND
or_result = a | b       # performs binary OR
xor_result = a ^ b      # performs binary XOR
not_result = ~a         # performs binary NOT
left_shift = a << 1     # performs binary left shift
right_shift = a >> 1    # performs binary right shift

print("a & b =", and_result)
# Rule: 1 & 1 = 1, otherwise 0.
# a = 0101 (5)
# b = 0011 (3)
# ------------
# &   0001 = 1


print("a | b =", or_result)
# Rule: 1 | 1 = 1, 1 | 0 = 1, otherwise 0.
# a = 0101 (5)
# b = 0011 (3)
# ------------
# |   0111 = 7

print("a ^ b =", xor_result)
# Rule: 1 ^ 1 = 0, 0 ^ 0 = 0, otherwise (not same equivalents to) 1.
# a = 0101 (5)
# b = 0011 (3)
# ------------
# ^   0110 = 6

print("~a =", not_result)
# Rule: Inverts all bits.
# a =  0101 (5)
# ~a = 1010 → which represents -6 in decimal

print("a << 1 =", left_shift)
# Rule: Shifts bits to the left, filling with 0s.
# a = 0101 (5)
# a << 1 = 1010 = 10


print("a >> 1 =", right_shift)
# Rule: Shifts bits to the right, filling with 0s.
# a = 0101 (5)
# a >> 1 = 0010 = 2