class Solution(object):
    def letterCombinations(self, digits):
        mapping = {'2': "abc",
                   '3': "def",
                   '4': "ghi",
                   '5': "jkl",
                   '6': "mno",
                   '7': "pqrs",
                   '8': "tuv",
                   '9': "wxyz"}

        combos = []
        for k in range(len(digits)-1, -1, -1):
            print(k)
            digit = digits[k]
            m=mapping[digit]
            combosF = combos
            combos = []
            if len(combosF)==0:
                for i in range(len(m)):
                    combos.append(m[i])
            else:
                for i in range(len(m)):
                    for c in combosF:
                        combos.append(m[i]+c)


        return combos
        """
        :type digits: str
        :rtype: List[str]
        """
