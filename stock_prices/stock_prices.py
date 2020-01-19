#!/usr/bin/python

import argparse


def find_max_profit(prices):

    max_gain = -2000
    max_loss = -2000
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[i] > prices[j]:
                if (prices[i] - prices[j]) * -1 > max_loss:
                    max_loss = (prices[i] - prices[j]) * -1

            else:
                if abs(prices[i] - prices[j]) > max_gain:
                    max_gain = abs(prices[i] - prices[j])
    if max_gain > max_loss:
        max_profit = max_gain
    else:
        max_profit = max_loss
    return max_profit


print(find_max_profit([100, 90, 80, 50, 20, 10]))
# if __name__ == '__main__':
#     # This is just some code to accept inputs from the command line
#     parser = argparse.ArgumentParser(
#         description='Find max profit from prices.')
#     parser.add_argument('integers', metavar='N', type=int,
#                         nargs='+', help='an integer price')
#     args = parser.parse_args()

#     print("A profit of ${profit} can be made from the stock prices {prices}.".format(
#         profit=find_max_profit(args.integers), prices=args.integers))
