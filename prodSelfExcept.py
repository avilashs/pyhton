def prodSelfExcept(nums):
    nums_mul = []
    for idx in range(0,len(nums)):
        subArr1 = nums[idx+1:]
        subArr2 = nums[:idx]
        prevMul = 1
        for num in subArr1:
            prevMul = prevMul* num
        for num in subArr2:
            prevMul = prevMul* num
        nums_mul.append(prevMul)
        prevMul=1
    return nums_mul

def test():
    arr = [1,2,3,4]
    print(prodSelfExcept(arr))
    arr = [0,1,2,3]
    print(prodSelfExcept(arr))
test()