class Solution:
    def nextPermutation(self, nums: List[int]) -> None:

        if len(nums) <= 2:
            return nums.reverse()


        i = len(nums)-2
        while i >= 0 and nums[i]>= nums[i+1]:

            i -= 1
        if i == -1:
            return nums.reverse()

        for j in range(len(nums)-1, i, -1):
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                break
        nums[i+1:] =  reversed(nums[i+1:])


        """
        Do not return anything, modify nums in-place instead.
        """
