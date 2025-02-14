#!/usr/bin/python

import argparse


def find_max_profit(prices):
    if len(prices) <= 1:
        return 0
    current_min = prices[0]
    current_max = prices[1]
    answer = current_max - current_min
    for i in range(1, len(prices)):
        if prices[i] > current_max:
            current_max = prices[i]
            answer = current_max - current_min
        elif prices[i] < current_min:
            current_min = prices[i]
    return answer


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
