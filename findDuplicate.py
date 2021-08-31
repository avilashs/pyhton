def findDuplicate(nums):
    nums.sort()
    prevNum = nums[0]
    for idx in range(1,len(nums)):
        if prevNum == nums[idx]:
            return prevNum
        prevNum = nums[idx]
        
        
def test():
    arr = [1,2,3,2]
    print(findDuplicate(arr))
    arr = [0,1,2,3]
    print(findDuplicate(arr))
test()