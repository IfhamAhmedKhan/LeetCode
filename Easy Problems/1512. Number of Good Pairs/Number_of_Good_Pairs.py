class Solution(object):
    def numIdenticalPairs(self, nums):
        pair = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    pair += 1
        return pair

