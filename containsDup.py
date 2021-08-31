def containsDup(arr):
    return len(arr) >len(set(arr))

def test():
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    print(containsDup(arr))
    arr = [5,4,-1,7,8]
    print(containsDup(arr))
test()