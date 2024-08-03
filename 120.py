class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}

        def helper(level: int, total: int, lastindex: int):
            if level == len(triangle):
                return total

            curtotalmin = float("inf")

            for i in range(lastindex, lastindex+1+1):
                v = triangle[level][i]

                if (level,i) in memo.keys():

                    h = total+memo[(level,i)]

                else:
                    h = helper(level+1, v, i)
                    memo[(level,i)] = h
                    h += total

                if h < curtotalmin:
                    curtotalmin = h

            return curtotalmin



        return helper(1, triangle[0][0], 0)
