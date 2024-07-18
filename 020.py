class Solution:

    def isValid(self, s: str) -> bool:

        start = ['(','{','[']
        end = [')','}',']']
        stack = []
        for i in range(len(s)):

            if s[i] in start:
                stack.append(s[i])
            else:
                for b in range(3):
                    if s[i] == end[b]:
                        if len(stack)==0:
                            return False
                        if stack[len(stack)-1]==start[b]:

                            stack = stack[:len(stack)-1]
                        else:
                            return False

        if len(stack) == 0:
            return True
        return False
