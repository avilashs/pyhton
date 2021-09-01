def numberToWord(n):
    if n > 9999:
        return "Please provide number between 1 and 9999."
    ret_s = ""
    #define maps 
    num_map = {0:"",
               1:"One",
               2:"Two",
               3:"Three",
               4:"Four",
               5:"Five",
               6:"Six",
               7:"Seven",
               8:"Eight",
               9:"Nine",
               10:"Ten",
               11:"Eleven",
               12:"Twelve",
               13:"Thirteen",
               14:"Fourteen",
               15:"Fifteen",
               16:"Sixteen",
               17:"Seventeen",
               18:"Eighteen",
               19:"Nineteen"           
    }
    tens_map = {2:"Twenty",
                3:"Thirty",
                4:"Forty",
                5:"Fifty",
                6:"Sixty",
                7:"Seventy",
                8:"Eighty",
                9:"Ninety"  
    }
    #thousands value 
    val = n//1000
    if val > 0:
        ret_s += num_map[val] + " Thousand "
    
    n = n - val*1000
    #hundreds value 
    val = n//100
    if val > 0:
        ret_s += num_map[val] + " Hundred "
    n = n - val*100
    if n in num_map:
          ret_s += num_map[n]
    else:
        #tens and one's value 
        val = n //10 
        ret_s += tens_map[val]  + num_map[n%10]
        
    return ret_s   
def test():
    # numberToWord(100000)
    # numberToWord(1000)
    # print(numberToWord(119))
    print(numberToWord(11199))
    # print(numberToWord(123))
    # print(numberToWord(311))
test()