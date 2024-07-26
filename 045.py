class Solution:
    def jump(self, nums: List[int]) -> int:
        store = {}

        def helper(i: int) -> int:

            if i >= len(nums) - 1:
                return 0

            if i in store:
                return store[i]


            minjumps = float('inf')
            for j in range(1, nums[i] + 1):
                result = helper(i + j)
                if result+1 < minjumps:
                    minjumps = result + 1

            store[i] = minjumps
            return minjumps

        return helper(0)
