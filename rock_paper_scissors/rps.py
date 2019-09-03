#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    def combine(arr, n):
        if n == 0:
            return [[]]
        if n == 1:
            return [['rock'], ['paper'], ['scissors']]
        previous_arr = combine(arr, n-1)
        arr = []
        for i in range(len(previous_arr)):
            arr.append(previous_arr[i] + ["rock"])
            arr.append(previous_arr[i] + ['paper'])
            arr.append(previous_arr[i] + ['scissors'])
        return arr

    answer = []
    return combine(answer, n)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
