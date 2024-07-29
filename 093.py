class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ips = []
        def backtrack(start:int, cur:str):
            if len(cur) == 4:
                if start == len(s):
                    ip = ""
                    for p in cur:
                        ip += p
                        ip += "."

                    ips.append(ip[0:len(ip)-1])
                return

            for i in range(1, 4):
                if start + i <= len(s):
                    num = s[start:start + i]
                    if (num[0] != '0' or num == "0") and int(num) in range(0,256):

                        backtrack(start + i, cur + [num])




        backtrack(0, [])
        return ips
