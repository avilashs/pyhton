def bestTimeStock(arr):
    buy = arr[0]
    maxProfit = 0
    for idx in range(1,len(arr)):
        maxProfit = max(maxProfit,arr[idx]-buy)
        buy = min(buy,arr[idx])
    return maxProfit

def test():
    arr = [10,7,5,8,11,9]
    print(bestTimeStock(arr))
    arr = [7,6,4,3,1]
    print(bestTimeStock(arr))
test()