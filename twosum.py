# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

def twoSum(nums,target):
    for idx in range(0,len(nums)):
        if target -nums[idx] in nums and idx != nums.index(target -nums[idx]):
            return [idx,nums.index(target -nums[idx])]
            
print(twoSum([2,7,11,15],9))