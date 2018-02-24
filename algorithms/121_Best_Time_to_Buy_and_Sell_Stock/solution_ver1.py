# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
import timeit


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        one pass, two variable, storing historical low point for buying, and one for rolling maximum profit
        """
        historical_low_price, current_best_deal = float('inf'), 0
        for price in prices:
            historical_low_price = min(historical_low_price, price)
            current_best_deal = max(current_best_deal, price - historical_low_price)
            return current_best_deal


def run():
    Solution().maxProfit([7, 1, 5, 3, 6, 4])


def main():
    timer = timeit.Timer('run()', "from __main__ import run")
    t = timer.timeit(1000)
    print(t)


if __name__ == '__main__':
    main()
