"""
    Put here some decorators for general usage

"""


def timeit(method):
    """
        execution time decorator
         may be useful to validate performance of a solution
    :param method:
    :return:
    """
    def timed(*args, **kw):
        # local import, bad practice but good way to import source only in place where you really need it
        import time
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print('%r  %2.2f ms' %
                  (method.__name__, (te - ts) * 1000))
        return result
    return timed


def _get_change_making_matrix(set_of_coins, r: int):
    m = [[0 for _ in range(r + 1)] for _ in range(len(set_of_coins) + 1)]
    for i in range(1, r + 1):
        m[0][i] = float('inf')  # By default there is no way of making change
    return m


def change_making(coins, n: int):
    """This function assumes that all coins are available infinitely.
    n is the number to obtain with the fewest coins.
    coins is a list or tuple with the available denominations.
    """
    m = _get_change_making_matrix(coins, n)
    for c in range(1, len(coins) + 1):
        for r in range(1, n + 1):
            # Just use the coin coins[c - 1].
            if coins[c - 1] == r:
                m[c][r] = 1
            # coins[c - 1] cannot be included.
            # Use the previous solution for making r,
            # excluding coins[c - 1].
            elif coins[c - 1] > r:
                m[c][r] = m[c - 1][r]
            # coins[c - 1] can be used.
            # Decide which one of the following solutions is the best:
            # 1. Using the previous solution for making r (without using coins[c - 1]).
            # 2. Using the previous solution for making r - coins[c - 1] (without
            #      using coins[c - 1]) plus this 1 extra coin.
            else:
                m[c][r] = min(m[c - 1][r], 1 + m[c][r - coins[c - 1]])
    return m[-1][-1]


given_coins = [25, 10, 1]
# print(change_making(given_coins, 30))
"stre".index('re',)

import sys


class Solution:
    def coinChange(self, coins, amount: int) -> int:
        results_ar = [self.minCoins(coins, len(coins[start:]), amount) for start in range(len(coins))]
        return min(results_ar)

    def minCoins(self, coins, m, V):

        # base case
        if (V == 0):
            return 0

        # Initialize result
        res = sys.maxsize

        # Try every coin that has smaller value than V
        for i in range(0, m):
            if (coins[i] <= V):
                sub_res = self.minCoins(coins, m, V - coins[i])

                # Check for INT_MAX to avoid overflow and see if
                # result can minimized
                if (sub_res != sys.maxsize and sub_res + 1 < res):
                    res = sub_res + 1

        return res if res != sys.maxsize else -1


given_coins = [2]
val = 3
# given_coins = [1, 2, 5]
# val = 11
print(Solution().coinChange(given_coins, val))