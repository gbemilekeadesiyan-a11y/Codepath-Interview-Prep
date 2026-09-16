"""
You are given a list of tuples, where each tuple contains a category and a value. Write a function to count how many items belong to each category.

Input: items = [("fruits", "apple"), ("vegetables", "carrot"), ("fruits", "banana")]
Output: {"fruits": 2, "vegetables": 1}


1. Understand (Input, Output, Core logic, Edge cases, tradeoffs and runtime complexities)

Input: 
Plan 


Implement



"""


def count_by_categories(items): # list of tuples [("fruits", "apple"), ("vegetables", "carrot"), ("fruits", "banana")]
    category_count ={}
    for item in items: # item --> ("fruits", "apple"), we acces it the same way as a list 
        item_category = item[0] # **key  "fruit"
        item_name = item [1] # "apple"
    