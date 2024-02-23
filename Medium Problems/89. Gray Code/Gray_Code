class Solution(object):
    def grayCode(self, n):
        if n == 0:
            return [0]
        result = []
        for i in range(2**n):
            result.append(i ^ (i >> 1))
        return result
