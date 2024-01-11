class Solution(object):
    def divide(self, dividend, divisor):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Handle special cases
        if divisor == 0:
            return INT_MAX if dividend > 0 else INT_MIN
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine the sign of the result
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        # Convert both dividend and divisor to positive
        dividend, divisor = abs(dividend), abs(divisor)

        # Initialize the quotient
        quotient = 0

        # Perform bitwise division
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= temp << 1:
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            quotient += multiple

        result = sign * quotient

        return min(max(result, INT_MIN), INT_MAX)
