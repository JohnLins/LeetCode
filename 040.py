class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def combine(start: int, path: List[int], result):
            if sum(path) > target:
                return result
            if sum(path) == target:
                result.append(path)
            prev = -1
            for i in range(start, len(candidates)):
                if candidates[i] == prev:
                    continue
                combine(i+1, path + [candidates[i]], result)
                prev = candidates[i]
            return result



        return combine(0, [], [])
