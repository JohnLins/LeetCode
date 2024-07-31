class Solution(object):
    def convert(self, s, numRows):
        zigzag = []
        dagO = numRows - 1
        if dagO == 0:
            return s

        k = 0
        while k < len(s):
            elem = []
            for h in range(numRows):
                if k < len(s):
                    if len(zigzag)%dagO==0:
                        elem.append(s[k])
                        k+=1
                    else:
                        if h == (numRows-1)-len(zigzag)%dagO:
                            elem.append(s[k])
                            k+=1
                        else:
                            elem.append(" ")
                else:
                    for _ in range(numRows-len(elem)):
                        elem.append(" ")
            zigzag.append(elem)


        output = ""
        for j in range(numRows):
            for i in range(len(zigzag)):
                char = zigzag[i][j]
                if char != " ":
                    output += char
        return output
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
