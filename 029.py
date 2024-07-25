
class Solution:

    def divide(self, dividend: int, divisor: int) -> int:
        neg = False
        numtimes = 0
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            neg = True

        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor:
            d = divisor
            stepsize = 1
            while dividend >= d:

                dividend -= d
                if neg:
                    numtimes -= stepsize
                else:
                    numtimes += stepsize
                stepsize += stepsize
                d += d


        if numtimes < -2**31:
            return -2**31
        if numtimes > 2**31 - 1:
            return 2**31 - 1


        return numtimes

#long way
class Solution:

    def divide(self, dividend: int, divisor: int) -> int:
        neg = False
        numtimes = 0
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            neg = True

        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor:
            dividend -= divisor
            if neg:
                numtimes -= 1
            else:
                numtimes += 1



        if numtimes < -2**31:
            return -2**31
        if numtimes > 2**31 - 1:
            return 2**31 - 1


        return numtimes
