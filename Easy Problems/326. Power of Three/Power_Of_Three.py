import math

class Solution(object):
    def isPowerOfThree(self, n):
        if n <= 0:
            return False
        log_result = math.log(n, 3)
        return abs(log_result - round(log_result)) < 1e-10


