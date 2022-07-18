def lengthOfLongestSubstring(s):
    maxLen = 0
    start = 0
    prevCharSet = set() 
    for chr in s:
        if chr in prevCharSet:
            start = 1
            prevCharSet = set(chr) 
        else:
            start += 1
            prevCharSet.add(chr)
            maxLen =max(maxLen,start)
    return maxLen


def longestSubstring(s):
    if len(s) < 2:
        return len(s)
    p1, p2 , longest, seen = 0,0,0,{}
    
    while p2 < len(s):
        # If we saw the char and it is in our current substring
        # example "abcdeafgh"
        #          1    2
        if s[p2] in seen and seen[s[p2]] >= p1:
            # Shrink the substring from the from (p1) until the char at p2 (+ 1 to exclude p2)
            p1 = seen[s[p1]] + 1
            # example "abcdeafgh"
            #           1   2
        else:
            seen[s[p2]] = p2
            p2 += 1
            longest = max(longest, p2-p1)
    return longest
    
print(longestSubstring("dvdf"))