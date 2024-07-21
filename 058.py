class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        begin = len(s)
        end = 0
        started = False
        for i in range(len(s)-1,-1,-1):
            if s[i] != " " and not started:
                begin = i
                started = True
            if (s[i] == " ") and started:
                end = i
                break
            if i == 0 and started:
                end = i-1
                break
        return begin-end
