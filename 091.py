class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0

        if len(s) == 1:
            return 1


        prevprev = 1
        prev = 1
        cur = 0

        for i in range(2, len(s) + 1):
            cur = 0

            if s[i - 1] != '0':
                cur += prev
            if int(s[i - 2:i]) in range(10,27):
                cur += prevprev

            prevprev = prev
            prev = cur


        return cur
