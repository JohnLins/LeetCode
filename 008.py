class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0

        start = 0
        neg = None



        while start < len(s):
            if s[start] == "-":
                if neg != None:
                    return 0
                neg = True

            if s[start] == "+":
                if neg != None:
                    return 0
                neg = False

            if s[start] not in  [" ", "-","+"]:
                break

            if s[start] == " " and neg != None:
                return 0

            start+=1


        if start == len(s):
            return 0

        if s[start] == "-":
            neg = True
            start += 1
        if s[start] == "+":
            neg = False
            start += 1


        integer = 0
        dec = 1
        for i in range(len(s)-1, start-1, -1):
            print(i)

            if s[i] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                integer = 0
                dec = 1
            else:
                integer += dec*int(s[i])
                dec *= 10

        if neg:
            integer *= -1



        if integer < -2**31:
            integer = -2**31
        if integer > 2**31 - 1:
            integer = 2**31-1

        return integer
