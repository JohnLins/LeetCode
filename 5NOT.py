#LONG WAY:
class Solution(object):
    def isPalindrome(self, s):
        for i in range(len(s)/2):
            if s[i] != s[len(s)-1-i]:
                return False
        return True

    def longestPalindrome(self, s):

        maxsubstring = ""
        for i in range(len(s)+1):
            for j in range(len(s)+1):
                substring = s[i:j]
                if self.isPalindrome(substring) and (len(substring) > len(maxsubstring)):
                    maxsubstring = substring
        return maxsubstring
        """
        :type s: str
        :rtype: str
        """
