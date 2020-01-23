#!/usr/bin/python


def making_change(amount, denominations, cache=[], loop_count=0):
    # initialize cache
    if cache == []:
        for i in range(amount):
            if i == 0:
                cache.append(1)
            cache.append(0)
    # set base case
    loop_count = loop_count + 1
    if len(denominations) == loop_count - 1:
        return cache[amount]
    # from coin to end of amount
    current_coin = denominations[loop_count - 1]
    # place the amount at higher_amount - current_coin in next array position
    for higher_amount in range(current_coin, amount + 1):
        previous_amount = cache[higher_amount - current_coin]
        cache[higher_amount] = cache[higher_amount] + previous_amount
    # recursive call to until all denominations have been compiled
    return making_change(amount, denominations, cache, loop_count)


print(making_change(100, [1, 5, 10, 25, 50]))
