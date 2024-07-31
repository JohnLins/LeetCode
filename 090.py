class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        numeach = {}
        for n in nums:
            if n not in numeach.keys():
                numeach[n] = 1
            else:
                numeach[n] += 1

        def correct(arr: List[int]) -> bool:
            d = numeach.copy()
            for a in arr:
                d[a] -= 1
                if d[a] < 0:
                    return False
            return True


        def backtrack(combos: List[List[int]])->List[List[int]]:
            if len(combos[-1]) == len(nums):
                return combos


            for i in range(len(combos)):
                for n in nums:
                    x = sorted(combos[i] + [n])
                    if x not in combos and correct(x):
                        combos.append(x)

            return backtrack(combos)



        return backtrack([[]])
