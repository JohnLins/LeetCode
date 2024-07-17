class Solution(object):
    def lengthOfLongestSubstring(self, s):

        past = set()
        start = 0
        end = 0
        for i in range(len(s)):
            if (i - end) >= (end-start):
                if (s[i] in past):
                    start = end
                    end = i
                    past = set()
                elif i==len(s)-1:
                    end = i

            past.add(s[i])

        print(s[start:end])
        return end-start
        """
        :type s: str
        :rtype: int
        """
