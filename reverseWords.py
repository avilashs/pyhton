def reverseWords(inp):
    str = ""
    inpArr=inp.split()
    for idx in range(len(inpArr)-1,-1,-1):
        str += inpArr[idx] +" "
    return str.strip()

def test():
    print(reverseWords("humanity is great"))

test()
