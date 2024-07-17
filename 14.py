class Solution(object):
    def longestCommonPrefix(self, strs):
        common = ""
        i = 0
        while True:
            allofthem = True
            for j in range(len(strs)):
                if not (i < len(strs[j]) and i < len(strs[0])):
                    allofthem = False
                    break
                if strs[j][i] != strs[0][i]:
                    allofthem = False

            if allofthem:
                common += strs[0][i]
            else:
                break

            i+=1
        return common
        """
        :type strs: List[str]
        :rtype: str
        """
