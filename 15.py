from collections import Counter
class Solution(object):
    def threeSum(self, nums):
        nums = list(sorted(nums))
        m = 1
        d=1
        c = nums[0]
        while d < len(nums):

            if nums[d] == c:
                if m >=3:

                    nums = nums[:d]+nums[d+1:]
                else:
                    m +=1
                    d+=1
            elif nums[d] != c:
                c = nums[d]
                m = 1
                d+=1


        triplets = set()
        for k in range(len(nums)):
            i = 0
            j = len(nums)-1

            while i != j and i < len(nums) and j >= 0:

                if i!=k and j!=k and nums[k]+nums[i]+nums[j]==0:
                    triple = [nums[i], nums[j], nums[k]]
                    triple.sort()
                    triplets.add(tuple(triple))
                if nums[k]+nums[i]+nums[j] > 0:
                    j-=1
                else:
                    i+=1


        return triplets


        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
