'''
String Manipulation: Built in Functions

.lower() "Hello How Are You" -> "hello how are you"

.upper() "Hello How Are You" -> "HELLO HOW ARE YOU"

.strip() " hello cory.    how.   are.   you.     " -> "hello cory.    how.   are.   you."

.replace("cat", "dog") "The cat is sleeping" -> "The dog is sleeping"




s.split() "apple banana orange" -> ["apple", "banana", "orange"] #automatically remove spaces**
"".join(words) ["apple", "banana", "orange"] -> "apple banana orange" # join string (glue)



.isalpha() returns True/False if the single character is a letter (a-z), ignore spaces, ignore numbers, ignore special characters

.isdigit() returns True if the single character is a number (0-9)
'''



username = "corybrooks123" #bob456
firstName = "Cory"
lastName = "Brooks"
email = "" 
code = "" 
signedInTime = "June 18th, 6:15pm"
print(f"Hello {username}, {firstName} has signed in at {signedInTime}. Thank you {username}")


print("Hello {}, {} has signed in at {}. Thank you {}".format(username, firstName, signedInTime, firstName))


'''
Given a string s containing words separated by spaces, reverse the order of the words. 
Remove extra spaces and ensure that words are separated by a single space in the output.

Input: s = "  the sky is  blue  "
Output: "blue is sky the"


1. Understand (input, output, core logic, edge cases)

input -> string (sentence), might have additional spaces
output -> string (reversed sentence), wont have any extra spaces

core logic: be given a string, remove extra spaces, cut up all of our individual words (splitting)
after splitting, we need to figure reversal logic (maybe we will start with a simple approach, and then add a restriction)
figure out how to glue (join, concatenate) the small strings back together
return the final string

2. Plan

1. defining our new function
2. splitWords = [], reversedString = ""
3.  .split() to split up our words (returning a list)
4. slicing approach to reverse (there are multiple approaches!)
5. after we reverse, we will join the words back together with " "
6. return the final string


3. Implement
'''
def reverse_words(sentence):
    splitWords = sentence.split() #["Hello", "how", "are", "you?"]
    reversedString = "" #return at the end + + +

    #reversedString = " ".join(splitWords[::-1]) #maybe interviewer says we cant do this

    for word in splitWords:
        reversedString = word + " " + reversedString

    return reversedString

print(reverse_words("Hello how are you"))