min_price, max_price, max_diff = None, None, 0
    min_idx, max_idx = None, None
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            diff = prices[j] - prices[i]
            if diff > max_diff:
                max_diff = diff
                min_price, max_price = prices[i], prices[j]
                min_idx, max_idx = i+1, j+1
    str1 =  str.format("{0} {1}".format(min_idx, prices[min_idx-1]))
    str2 =  str.format("{0} {1}".format(max_idx, prices[max_idx-1]))
    print(str1)
    print(str2)