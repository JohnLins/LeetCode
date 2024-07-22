class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x < 0:
            neg = True
            x = abs(x)
        num = str(x)

        reversednum = ""
        for i in range(len(num)-1, -1,-1):
            reversednum += num[i]


        v = int(reversednum) * (-1 if neg else 1)

        if v < -2**31 or v > 2**31 - 1:
            return 0

        return v
