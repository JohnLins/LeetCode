class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        combos = []
        def backtrack(i,cur):
            if len(cur) == k:
                combos.append(cur)
                return

            for j in range(i, n+1):
                backtrack(j+1, cur + [j])



        backtrack(1, [])
        return combos
