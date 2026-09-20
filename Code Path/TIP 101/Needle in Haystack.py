""" Given two strings needle and haystack.
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack   


Understand: Input: A string which is (needle), (haystack). Return the index or position. 
            Edge Cases: If (needle) is greater than (haystack) we would return -1 and if needle is not in haystack we return -1, Special characters are not allowed. 

Plan: sadbutsad we are looking for sad, we have to indicate the first positon sad occurs in haystack. store the place position of needle and then use the index that needle takes and then use it to find other parts of haystack that it is found. 
sadbutnotsgaidetsaid
said
"""

def strStr(haystack,needle):
    if not needle or haystack:
        return -1 
        
    if len(needle) > len(haystack):
        return -1 
    
    
    for i in range(len(haystack) - len(needle)+ 1 ):  # the lenght of needle in haystack
        if haystack[i:i +len(needle)] == needle:      # Are the characters equal?
            return i 
        
    return -1  

print(strStr("sadbutnotsgaidetsaid", "said"))
    
