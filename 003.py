class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<=1:
            return len(s)
        maxlen = 0
        last = 0
        happened = {}
        i = 0
        while i < len(s):
            if i == len(s)-1 or s[i] in happened.keys():

                diff = i-last + (1 if i == len(s)-1 and s[i] not in happened.keys() else 0)
                if diff > maxlen:
                    maxlen = diff
                if s[i] in happened.keys():
                    i = happened[s[i]]+1

                last = i
                happened = {}


            happened[s[i]] = i
            i+=1
        return maxlen
