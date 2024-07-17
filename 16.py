class Solution(object):
    def threeSumClosest(self, nums, target):

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


        mostsimilar =nums[0]+nums[1]+nums[len(nums)-1]
        for k in range(1,len(nums),1):
            i = 0
            j = len(nums)-1

            while i != j and i < len(nums) and j >= 0:

                if i!=k and j!=k and abs(nums[k]+nums[i]+nums[j] - target) <= abs(mostsimilar-target):
                    triple = [nums[i], nums[j], nums[k]]
                    mostsimilar = sum(triple)

                if nums[k]+nums[i]+nums[j] > target:
                    j-=1
                else:
                    i+=1

        return mostsimilar



        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
