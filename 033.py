class Solution:
    def search(self, nums: List[int], target: int) -> int:


        orig = nums.copy()
        pivot = 0
        i = 0
        j = len(nums)-1


        if nums[i] > nums[j] :
            step = int((j-i)/4)
            while nums[i] >= nums[j] and step > 0:
                if nums[i] < nums[i+step]:
                    i += step
                if nums[j] > nums[j-step]:
                    j -= step
                step = int((j-i)/4)

            while nums[i] >= nums[j] and i<j and nums[j] > nums[j-1]:
                j -= 1
            pivot = j

        pivotrightlen = len(nums[pivot:])
        pivotleftlen = len(nums[:pivot])
        nums = nums[pivot:] + nums[:pivot]


        low = 0
        high = len(nums)-1


        print(orig)
        while low <= high:
            mid = int(low + (high-low)//2)

            if target == nums[mid]:
                if mid+pivotleftlen < len(orig) and orig[mid+pivotleftlen] == target:
                    return mid+pivotleftlen
                else:
                    return mid-pivotrightlen


            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1

        return -1
