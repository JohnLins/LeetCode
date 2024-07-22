class Solution:
    def addBinary(self, a: str, b: str) -> str:

        tostr = {0:'0', 1:'1'}

        if len(a) > len(b):
            a,b = b,a
        carry = 0
        for i in range(len(b)):
            j = len(b)-i-1
            x= (int(a[len(a)-i-1]) if len(a)-i-1 >= 0 else 0) + int(b[j]) + carry

            carry = (int)(x/2)

            x=x%2


            b = b[:j] + tostr[x] + b[j+1:]

        while carry > 0:
            b = tostr[carry%2] + b
            carry = (int)(carry/2)

        return b
