import sys
class Solution:
    def maxProfit(self, prices):
        """
        :type x: int array
        :rtype: int
        """
        buy = 0
        sell = buy + 1
        maxDays = len(prices) - 1
        maxProfit = 0

        while buy < maxDays:
            while sell <= maxDays:
                if(prices[sell] > prices[buy]):
                    profit = prices[sell] - prices[buy]
                    if profit > maxProfit:
                        maxProfit = profit
                sell += 1
            buy += 1
            sell = buy + 1
        return maxProfit

    def maxProfitFaster(self, prices):
        """
        This will be done in O(n) due to only 1 loop.
        """

        minPrice = sys.maxsize
        maxProfit = 0

        for i in range(0, len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            elif prices[i] - minPrice > maxProfit:
                maxProfit = prices[i] - minPrice

        return maxProfit

test = Solution()

print(test.maxProfit([7,1,5,3,6,4]))
print(test.maxProfit([7,6,4,3,1]))

print(test.maxProfitFaster([7,1,5,3,6,4]))
print(test.maxProfitFaster([7,6,4,3,1]))
