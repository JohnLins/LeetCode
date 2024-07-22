class Solution:
    store = {}
    def helper(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1

        if n not in self.store:
            self.store[n] = self.helper(n-1) + self.helper(n-2)

        return self.store[n]

    def climbStairs(self, n: int) -> int:

        return self.helper(n)

