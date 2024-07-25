class Solution:
    def longestPalindrome(self, s: str) -> str:

        def odd(i: int,j: int) -> (int,int):
            if s[i] != s[j]:
                return i,i

            if i - 1 >=0 and j+1 <= len(s)-1 and s[i-1] == s[j+1]:
                return odd(i-1, j+1)

            return i,j

        maxlen = 0
        maxstr = ""
        for i in range(len(s)):
            if i != len(s)-1:
                start, end = odd(i, i+1)
                end+=1
                l = end-start
                if l > maxlen:
                    maxlen = l
                    maxstr = s[start:end]

            start, end = odd(i, i)
            end += 1
            l = end - start
            if l > maxlen:
                maxlen = l
                maxstr = s[start:end]


        return maxstr



