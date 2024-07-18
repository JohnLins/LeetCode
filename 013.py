class Solution(object):
    def romanToInt(self, s):
        total = 0
        i = 0
        while i < len(s):

            if s[i] == 'I':
                total += 1
                if i+1 < len(s):
                    if s[i+1] == 'V':
                        total += 3
                        i+=1
                    elif s[i+1] == 'X':
                        total += 8
                        i+=1

            elif s[i] == 'V':
                total += 5

            elif s[i] == 'X':
                total += 10
                if i+1 < len(s):
                    if s[i+1] == 'L':
                        total += 30
                        i+=1
                    elif s[i+1] == 'C':
                        total += 80
                        i+=1

            elif s[i] == 'L':
                total += 50

            elif s[i] == 'C':
                total += 100
                if i+1 < len(s):
                    if s[i+1] == 'D':
                        total += 300
                        i+=1
                    elif s[i+1] == 'M':
                        total += 800
                        i+=1


            elif s[i] == 'D':
                total += 500

            elif s[i] == 'M':
                total += 1000

            i+=1

        return total
        """
        :type s: str
        :rtype: int
        """
