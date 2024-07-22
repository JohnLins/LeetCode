class Solution:

    def nextPermutation(self, l: List[int]) -> List[int]:
        nums = l.copy()
        if len(nums) <= 2:
            nums[:] = reversed(nums[:])
            return nums


        i = len(nums)-2
        while i >= 0 and nums[i]>= nums[i+1]:

            i -= 1
        if i == -1:
            nums[:] = reversed(nums[:])
            return nums

        for j in range(len(nums)-1, i, -1):
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                break
        nums[i+1:] =  reversed(nums[i+1:])

        return nums

    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        permutations = []
        i = 1
        q = len(nums)
        p = q
        x = nums
        while i <= p and x != None:
            permutations.append(x)

            x = self.nextPermutation(x)


            if q > 1:
                q-=1
                p *= q

            i+=1

        return permutations

