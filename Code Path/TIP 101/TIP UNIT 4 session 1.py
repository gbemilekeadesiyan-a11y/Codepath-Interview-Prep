'''
New stages today 
Match: Technique and similar or "simple" versions of the question
Review: Check for errors, edge cases and chances to optimize
Evaluate: Review the question's requirements, (think about runtime, will introduce this in our next class)

Question:
Given a string s, determine if it can become a ******palindrome by removing at most one character.********
A palindrome is a word, phrase, or sequence that reads the same backward as forward.








Input: s = "abca"
Output: True

1. Understand: (input, output, core logic, edge cases)

input: string (sentence)
output: True or False (boolean)
core logic: just a normal palindrome but one letter can be skipped. 
edge cases: (data type of your input) input is None, numbers, or special characters, input only 1 letter, casing

2. Match: (techniques or approahces data structures that seem related, similar / simpler version of the question)

Technique: Two pointer, moving pointers closer together while checking for equality
Data structures: string, indicies (integers)
Similar problem: Original Palindrome (all letters cant be skipped)


3. Plan

0. Matched this to original palindrome, ********lets start with this plan, and then identify how to change it (we will add the requirement later)
1. define our new function (input sentence)
2. new variables, left and right pointer (integers)
3. while loop (moving left and right closer to each other, ) #End condition when the pointers pass each other
4. original palindrome: if the letters dont match, we will return False
5. if all letters were equal, we can return True after the while loops 
6. we do need to continue our plan to add our additional requiement
7. we can kindof reuse normal palindrome logic, but just figure out how to get the 2 "skip" versions of the string



3. Implement
4. Review
5. Evaluate




Example
A B B C B B A D
L             R
-> skip left letter: B B C B B A D
-> skip right letter: A B B C B B A    (**)

'''
# skipped edge cases due to time, please consisder them when reviewing this code
def valid_palindrome(sentence):
    left = 0
    right = len(sentence) - 1

    while(left < right):
        #if the letters dont match here
        if(sentence[left] != sentence[right]):
            #instead of returning false, check 2 versions of new strings
            
            #check the skip left version, 2 variables + while loop
            skip_left_l = left + 1
            skip_left_r = right
            while(skip_left_l < skip_left_r and sentence[skip_left_l] == sentence[skip_left_r]): #stops when things arent equal
                skip_left_l += 1
                skip_left_r -= 1


            # check the skip right version  2 variables + while loop
            skip_right_l = left
            skip_right_r = right - 1
            while(skip_right_l < skip_right_r and sentence[skip_right_l] == sentence[skip_right_r]): #stops when things arent equal
                skip_right_l += 1
                skip_right_r -= 1


            #check integer pointers
            #maybe skip left is correct, maybe skip right is correct, maybe neither
            return(skip_left_l >= skip_left_r or skip_right_l >= skip_right_r) #boolean ,if left passed right, that means the skip version is valid!
        
        else:
            left += 1
            right -= 1
    
    return True

print(valid_palindrome("azzbccba"))