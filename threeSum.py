def find_sum_of_three_v3(arr,s):
    arr.sort()
    def twoSum(arr,ss):
        for idx in range(0,len(arr)-1):
            if ss-arr[idx] in arr[idx+1::]:
                return True
        return False
    for idx in range(0,len(arr)-1):
        if twoSum(arr[idx+1::],s-arr[idx]):
            return True
    return False


def test():
  arr = [-25, -10, -7, -3, 2, 4, 8, 10]
#   print(find_sum_of_three_v3(arr, -8)) 
#   print(find_sum_of_three_v3(arr, -25))
#   print(find_sum_of_three_v3(arr, 0))
#   print(find_sum_of_three_v3(arr, -42))
#   print(find_sum_of_three_v3(arr, 22))
#   print(find_sum_of_three_v3(arr, -7))
#   print(find_sum_of_three_v3(arr, -3)) 
#   print(find_sum_of_three_v3(arr, 2)) 
#   print(find_sum_of_three_v3(arr, 4)) 
#   print(find_sum_of_three_v3(arr, 8))
#   print(find_sum_of_three_v3(arr, 7)) 
  print(find_sum_of_three_v3(arr, 1))
  
test()