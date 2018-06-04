class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int

                             |
        |        |  |     |
              |        |
           |                    |
        1  2  3  4  5  6  7  8  9

        buy on day 2 and sale on day 8 gives less profit than
        buy on day 2 sale on day 4 and buy again on day 6 and sale on day 8.
           => doing as many smaller monotonic increasing transactions better than doing on with up and downs in it

        # note if the transaction is not free, then this is problematic.
        """
        profit = 0
        for idx, price in enumerate(prices[:-1]):
            profit += (prices[idx + 1] - price) if prices[idx + 1] - price > 0 else 0
        return profit