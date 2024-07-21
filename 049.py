class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = []
        groupchars = []

        for i in range(len(strs)):
            dic = {}
            for j in range(len(strs[i])):
                if strs[i][j] in dic.keys():
                    dic[strs[i][j]] += 1
                else:
                    dic[strs[i][j]] = 1

            already = False
            for k in range(len(groupchars)):
                if dic == groupchars[k]:
                    groups[k].append(strs[i])
                    already = True
                    break
            if not already:
                groups.append([strs[i]])
                groupchars.append(dic)

        return groups
