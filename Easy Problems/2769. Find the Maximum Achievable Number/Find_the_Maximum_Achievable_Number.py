class Solution(object):
    def theMaximumAchievableX(self, num, t):
        x = 0
        for i in range(t):
            num = num + 1
            x = num - 1

        return num+t