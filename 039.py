class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:


        def combine(start: int, path: List[int], result: List[int]):
            if sum(path) > target:
                return result
            if sum(path) == target:
                result.append(path)
            for i in range(start, len(candidates)):
                combine(i, path + [candidates[i]], result)
            return result

        return combine(0, [], [])


