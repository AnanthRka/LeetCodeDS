def maxProfit( prices: list[int]) -> int:

    if len(prices)== 1:
        return 0
    
    left = profit = 0
    right = 1

    while right < len(prices):
        difference = prices[right] - prices[left]

        if difference < 0:
            left = right
        else:
            profit = max(profit, difference)
        right += 1
    return profit

print(maxProfit([7,1,4,5,6,3]))