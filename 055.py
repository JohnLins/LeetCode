class Solution:
    def canJump(self, nums: List[int]) -> bool:
        store = {}
        def helper(i:int) -> bool:

            if i == len(nums)-1:
                return True
            if i >= len(nums):
                return False

            if i in store:
                return store[i]


            for j in range(nums[i], 0, -1):

                h = helper(i+j)
                store[i] = h
                if h:
                    return True


            return False

        return helper(0)
