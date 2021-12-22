def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    l = len(nums)
    res = [1] * l
    for i in range(1, l):
        res[i] = res[i - 1] * nums[i - 1]
    r = 1
    for i in range(l - 1, -1, -1):
        res[i] *= r
        r *= nums[i]
    return res