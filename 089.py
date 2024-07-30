class Solution:
    def grayCode(self, n: int) -> List[int]:

        output  = ['0','1']
        for i in range(n-1):
            appendzeros = output.copy()
            appendones = output.copy()[::-1]
            for j in range(len(output)):
                appendzeros[j] = "0"+appendzeros[j]
                appendones[j] = "1"+appendones[j]

            output = appendzeros + appendones

        for i in range(len(output)):
            output[i] = int(output[i],2)

        return output

