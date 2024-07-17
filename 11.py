class Solution(object):
    def maxArea(self, height):

        maxA = 0
        i=0
        j = len(height)-1
        while i != j:
            area = (j - i)*min(height[i], height[j])
            if area > maxA:
                    maxA = area
            if height[i] < height[j]:
                i+=1
            else:
                j-=1


        return maxA
        """
        :type height: List[int]
        :rtype: int
        """





#Slow way:
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
