class Solution:
    def numTrees(self, n: int) -> int:
        a=[1]
        for i in range(1, n+1):
            a.append(0)
            for j in range(i):
                left = j
                right = i-j-1
                a[i] += a[left] * a[right]
        return a[-1]
