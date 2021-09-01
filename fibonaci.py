fib_dict = {}
def fibonaci(n):
    if n in fib_dict:
        return fib_dict[n]
    if n in (0,1,2):
        return 1
    val= fibonaci(n-1) + fibonaci(n-2)
    fib_dict[n] = val
    return val

def test():
    print(fibonaci(20))

test()