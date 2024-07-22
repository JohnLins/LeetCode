class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1 or x == 0:
            return x

        low = 0
        high = x-1

        for i in range(50):
            i = (low+(high-low)/2)
            print(low, i, high)
            if i*i < x:
                low = i
            elif i*i > x:
                high = i
            elif int(i) * int(i):
                return (int)(i)


        return (int)(high)
