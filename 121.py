class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = prices[0]
        maxdiff = float("-inf")



        for i in range(len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]

            if prices[i]-minprice > maxdiff:
                maxdiff = prices[i]-minprice


        return maxdiff
