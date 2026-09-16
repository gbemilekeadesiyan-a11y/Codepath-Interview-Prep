'''Given a list of strings words, group the strings that are anagrams of each other.


Input: words = ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]



1) Understand (Input, Output, edge cases, logic, tradeoffs (readability vs speed))

Input: words = ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
------

2) Plan 
1. defione the function
2. New Variables (new dictionary {} )
3. Iterate through input words using a for loop
4. Figure out how to get anagrams representation/flag/check
5. Implement the dictionary check (have we seen the key (anagram) before, yees or no?)
6. Return the grouped list
------

\\ Implement

'''
def group_anagram(words):
    anagram_dictionary={} # "aet" -> [ate, eat, tea]
    
    for word in words:
        anagram_representation = str(sorted(word.lower())) # ['a', 'e','t'], KEY
        # dictionary key has to be immutable meaning it cannot be a list, it needs a string or a tuple
        if anagram_representation not in anagram_dictionary: # first time seeing this exact word or anagram
            anagram_dictionary[anagram_representation] = [word]
        else:
            anagram_dictionary[anagram_representation].append(word) # add to a lsit
    return anagram_dictionary.values()

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagram(words)) 