#timeout
class Solution(object):
    def maxArea(self, height):

        maxA = 0
        for i in range(len(height)):
            for j in range(i, len(height), 1):
                area = (j - i)*min(height[i], height[j])
                if area > maxA:
                    maxA = area
        return maxA
        """
        :type height: List[int]
        :rtype: int
        """
