#time limit
class Solution:
    def search(self, nums: List[int], jumps:int, i:int) -> int:
        if i == len(nums)-1:
            return jumps
        elif i > len(nums)-1 or nums[i] == 0:
            return -1

        branches = []
        for j in range(nums[i],0,-1):

            b = self.search(nums,jumps+1,i+j)

            if b != -1:
                branches.append(b)
        if len(branches) == 0:
            return -1
        return min(branches)


    def jump(self, nums: List[int]) -> int:
        return self.search(nums,0,0)
