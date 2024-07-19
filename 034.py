class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:


        high = len(nums)-1
        low = 0


        while True:
            if low > high:
                return [-1,-1]


            i = low + (high - low) // 2

            if nums[i] < target:
                low = i+1
            elif nums[i] > target:
                high = i-1
            elif nums[i] == target:

                break




        i = low
        j = high

        while i <= j:

            if nums[i] == target and (i-1 < low or nums[i-1] != target) and nums[j] == target and (j+1 > high or nums[j+1] != target):
                return [i,j]

            if nums[i] >= target:
                if (i-1 >= low and nums[i-1] == target):
                    i -= 1
            else:
                i += (int)( (j-i)/4+1  )



            if nums[j] <= target:
                if (j+1 <= high and nums[j+1] == target):
                    j += 1
            else:
                j -= (int)((j-i)/4+1)


            print(i,j)

        return [-1,-1]

