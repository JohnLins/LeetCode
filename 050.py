class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 1:
            x = 1/x
            n = -n

        if n % 2 == 0:
            t = self.myPow(x,n/2)
            return t*t
        else:
            return x * self.myPow(x, n-1)
