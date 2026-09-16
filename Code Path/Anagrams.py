"Anagrams"


def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t): 
        return False

    countS, countT = {}, {}
    for letter in range(len(s)):
        countS[s[letter]] = 1 + countS.get(countS[letter],0)
        countT[t[letter]] = 1 + countT.get(countT[t[letter],0])
    return countS == countT 





def isAnagram(s, t): 
    if len(s) != len(t):
        return False 

    countS, countT = {}, {}  #Initialise a tracking Dictionary
    for letter in range(len(s)):
        countS[s[letter]] = 1 + countS.get(s[letter], 0)   #Add content to the dictionary using thes reference string(s) since len(s) == len(t)
        countT[t[letter]] = 1 + countT.get(t[letter],0)
    return countS == countT  



