class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            minval = nums[i]
            minindex = i
            for j in range(i, len(nums)):
                if nums[j] < minval:
                    minval = nums[j]
                    minindex = j

            nums[i], nums[minindex] = nums[minindex], nums[i]

        """
        Do not return anything, modify nums in-place instead.
        """
