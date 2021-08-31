def mergeintervals(arr):
    retArr = []
    start_min,end_max = arr[0][0],arr[0][1]
    for idx in range(1,len(arr)):
        if end_max >= arr[idx][0]:
            end_max = max(end_max,arr[idx][1])
        else:
            retArr.append([start_min,end_max])
            end_max = arr[idx][1]
            start_min = arr[idx][0]
    retArr.append([start_min,end_max])
    return retArr
def test():
    intervals = [[1,4],[4,5]]#[[1,3],[2,6],[8,10],[15,18]]
    print(mergeintervals(intervals))
test()
    
