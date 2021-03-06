"""
You might know some pretty large perfect squares. But what about the NEXT one?

Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

If the parameter is itself not a perfect square then -1 should be returned. You may assume the parameter is non-negative.

Perfect Square;
Examples:

find_next_square(121) --> returns 144
find_next_square(625) --> returns 676
find_next_square(114) --> returns -1 since 114 is not a perfect square
"""
import math
def find_next_square(n):
    root = math.pow(n, 0.5)
    if root.is_integer():
        return math.floor((root + 1) ** 2)
    else:
        return -1
