class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums)==0:
            return 0

        i = 0
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
            else:
                i+=1
        print(nums)
        return len(nums)
