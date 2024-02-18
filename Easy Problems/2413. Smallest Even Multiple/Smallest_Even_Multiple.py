class Solution(object):
    def smallestEvenMultiple(self, n):
        if (n%2==0):
            return n
        elif (n%2==1):
            if (n<2):
                return 2
            else:
                return 2*n
        