def buy_sell_stock(prices):
    '''
    Given an array prices where prices[i] is the price of a given stock on the ith day.
    Return a profit while buying a share at lowest price and selling it in a future day, 
    Buy day and sell day
    '''
    lowest_price = prices[0]
    for price in prices:
        if price < lowest_price:
            lowest_price = price
        lowest_price_day = prices.index(lowest_price) + 1
    highest_price = lowest_price

    for i in prices[lowest_price_day - 1:]:
        if i > highest_price:#
            highest_price = i
        highest_price_day = prices.index(highest_price) + 1
    
    if highest_price_day == lowest_price_day:
        return "No profit"
    else:
        return f'Profit: {highest_price-lowest_price}, Day Buy: {lowest_price_day}, Day Sell: {highest_price_day}'

#Testing: --> uncomment below
prices1 = [7,1,5,3,6,1]
prices2 = [7,6,4,3,1]
print(buy_sell_stock(prices=prices1))
print(buy_sell_stock(prices=prices2))