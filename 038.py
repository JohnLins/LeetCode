class Solution:


    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"


        s = self.countAndSay(n-1)

        rle = ""
        if s != "":
            current = ""
            times = 0
            for i in range(len(s)):
                if current == "":
                    current = s[i]
                if s[i] == current:
                    times += 1
                else:
                    rle += str(times)+current
                    current = s[i]
                    times = 1

            rle += str(times)+current
        return rle
