ret_dict = {}
def climbStairs(n):
    if n in ret_dict:
            return ret_dict[n]
    if n == 1:
        return 1
    if n == 2:
        return 2
    val = climbStairs(n-1) + climbStairs(n-2)
    ret_dict[n] = val
    return val

print(climbStairs(int(input())))