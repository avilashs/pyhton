#Given a list of elements, find the first unique element
def firstUniqueElement(lst):
    elementDict = {}
    for item in lst:
        if item in elementDict:
            elementDict[item] += 1
        else:
            elementDict[item] = 1
    for item in elementDict:
        if elementDict[item] == 1:
            return item
    return None

def firstUniqueElementBrute(lst):
    for item in lst:
        if lst.count(item) ==1 :
            return item
    return None
print(firstUniqueElement(["a", "b", "d", "x", "x", "a"]))

print(firstUniqueElementBrute(["a", "b", "d", "x", "x", "a"]))