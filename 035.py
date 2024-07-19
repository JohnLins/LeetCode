class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        i = (int)(low + (high-low)/2)
        while low <= high:


            i = (int)(low + (high-low)/2)


            if nums[i] == target:
                return i
            elif nums[i] < target:
                low = i+1
            elif nums[i] > target:
                high = i-1


        if nums[i] < target:
            return i+1
        return i
