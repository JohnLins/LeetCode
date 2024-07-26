class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        cursum = 0
        maxsum = nums[0]
        for i in range(len(nums)):
            if cursum < 0:
                cursum = nums[i]
            else:
                cursum += nums[i]
            if cursum > maxsum:
                maxsum = cursum



        return maxsum
