class Solution(object):
    def arrangeCoins(self, n):
        # Using the pattern formula I have identify
        k = int(((8 * n + 1)**0.5 - 1) / 2)
        return k