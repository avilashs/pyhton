def maxSubArr(arr):
    currSum = maxSum = arr[0]
    for idx in range(1,len(arr)):
        currSum = max(currSum+arr[idx] , arr[idx]);
        maxSum = max(currSum,maxSum)
    return maxSum

def test():
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    print(maxSubArr(arr))
    arr = [5,4,-1,7,8]
    print(maxSubArr(arr))
test()