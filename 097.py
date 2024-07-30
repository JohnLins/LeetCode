class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        store = {}

        def helper(i: int, j:int, k:int)->bool:
            if (i, j) in store:
                return store[(i, j)]

            if k == len(s3):
                return i == len(s1) and j == len(s2)

            if i < len(s1) and s1[i] == s3[k] and helper(i + 1, j, k + 1):
                store[(i, j)] = True
                return True

            if j < len(s2) and s2[j] == s3[k] and helper(i, j + 1, k + 1):
                store[(i, j)] = True
                return True

            store[(i, j)] = False
            return False

        return helper(0, 0, 0)
