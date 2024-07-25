class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        appeared = {}
        if len(nums) <= 1:
            return len(nums)
        i = 1
        appeared[nums[0]] = 1

        prev = nums[0]
        while i < len(nums):

            if nums[i] in appeared.keys():
                appeared[nums[i]] += 1
            else:
                appeared[nums[i]] = 1

            print(i, nums)
            if nums[i] == prev and appeared[nums[i]] >= 3:
                print(appeared, i, nums)
                del nums[i]

            else:
                prev = nums[i]
                i+=1

        return len(nums)

