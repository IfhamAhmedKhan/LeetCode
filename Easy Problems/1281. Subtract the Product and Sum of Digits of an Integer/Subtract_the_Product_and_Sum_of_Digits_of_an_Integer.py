class Solution(object):
    def subtractProductAndSum(self, n):
        digits_string = str(n)
        digit_sum = sum(int(digit) for digit in digits_string)
        digit_product = 1
        for digit in digits_string:
            digit_product *= int(digit)
        return digit_product - digit_sum