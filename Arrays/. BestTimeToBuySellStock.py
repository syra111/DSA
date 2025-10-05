# Best Time to Buy and Sell Stock
# Problem link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

def maxProfit(prices):
    min_price = float('inf')   
    max_profit = 0             

    for price in prices:
        
        if price < min_price:
            min_price = price
        
        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print("Maximum Profit:", maxProfit(prices))  
