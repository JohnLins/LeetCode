class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False

        arr = []
        while x != 0:
            arr.append(x%10)
            x = x/10
        print(arr)

        for i in range(len(arr)/2):
            if arr[i] != arr[len(arr)-1-i]:
                return False
        return True
        """
        :type x: int
        :rtype: bool
        """
