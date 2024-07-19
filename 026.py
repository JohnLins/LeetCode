class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0:
            return nums

        current = nums[0]
        i = 1
        while i < len(nums):
            if nums[i] == current:
                del nums[i]
            else:
                current = nums[i]
                i+=1
        print(nums)
        return len(nums)
