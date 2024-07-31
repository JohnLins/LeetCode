class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def backtrack(combos: List[List[int]])->List[List[int]]:
            if len(combos[-1]) == len(nums):
                return combos


            for i in range(len(combos)):
                for n in nums:
                    x = sorted(combos[i] + [n])
                    if n not in combos[i] and x not in combos:
                        combos.append(x)

            return backtrack(combos)



        return backtrack([[]])
