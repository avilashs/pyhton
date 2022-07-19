def numPairsDivisibleBy60(arr):

    dct = {}
    count = 0
    target = 60
    for i,v in enumerate(arr):
        if v%60 == 0:
            count += 1
        else:
            count += dct.get(target-v%60,0)
            dct[v%60] = dct.get(v%60,0)+1
    return count
        

print(numPairsDivisibleBy60([30,20,150,100,40]))