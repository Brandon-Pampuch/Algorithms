#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


start = 0


def eating_cookies(n, cache=[]):
    global start
    if n > start:
        start = n
    if start == 3:
        return 4
    if start == 2:
        return 2
    if start < 2:
        return 1
    if n == 0:
        cache.append(1)
    if len(cache) == 1:
        cache.append(1)
    if len(cache) == 2:
        cache.append(2)
    if len(cache) > 2:
        cache.append(cache[len(cache) - 1] +
                     cache[len(cache) - 2] + cache[len(cache) - 3])
    if len(cache) == start:
        return cache[len(cache) - 1] + cache[len(cache) - 2] + cache[len(cache) - 3]
    return eating_cookies(n - 1, cache)


print(eating_cookies(4))
# if __name__ == "__main__":
#     if len(sys.argv) > 1:
#         num_cookies = int(sys.argv[1])
#         print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
#             ways=eating_cookies(num_cookies), n=num_cookies))
#     else:
#         print('Usage: eating_cookies.py [num_cookies]')
