from collections import deque 

# Tree Node class
def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1 

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root

class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right
        

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)
         
# Understand:
# Input: A TreeNode object
# Output: int
# We want to visit every node, and evaluate whether the node.val is odd or even
# If it is odd, we increment the count of our final answer by 1
# return ans

# Plan
# dfs (recursion) to traverse every node in the given root
# ans variable outside of the inner function scope to keep track of the odd numbers
# we want to count the current node.val's parity, so we wanna do preorder
# traverse through node.left and node.right
# outside of the inner func, we wanna call it and return ans

# Implementation
def count_odd_splits(root):
    ans = 0
        
    def dfs(node: TreeNode):
        nonlocal ans
        if not node:
            return
        
        if node.val % 2 == 1:
            ans += 1
        
        dfs(node.left)
        dfs(node.right)
    
    dfs(root)
    return ans

# Using build_tree() function included at top of page
'''
values = [2, 3, 5, 6, 7, None, 12]
monstera = build_tree(values)

print(count_odd_splits(monstera))
print(count_odd_splits(None))
'''


#Problem 2
"""
UNDERSTAND:
Input: the root node and the target plant as string
Output: boolean 
Edge Cases: if tree is empty return false

Plan:
check if root node is none -> if so return false
check if root is the target: return True

if root.val < target: 
    find_flower(inventory.right, target)
else:
    find_flower(inventory.left, target)

"""
def find_flower(inventory, name):
    if inventory == None:
        return False
    if inventory.val == name: 
        return True

    if inventory.val < name: 
        return find_flower(inventory.right, name)
    else:
        return find_flower(inventory.left, name)

# using build_tree() function at top of page
values = ["Rose", "Lilac", "Tulip", "Daisy", "Lily", None, "Violet"]

garden = build_tree(values)

print(find_flower(garden, "Lilac"))  
print(find_flower(garden, "Sunflower")) 

def non_bst_find_flower(root, name):
    if root is None:
        return False
    
    if root.val == name:
        return True

    return non_bst_find_flower(root.left, name) or non_bst_find_flower(root.right, name)






# Problem 4 
"""def add_plant(collection, name):
    if not collection:
        return TreeNode(name)
    
    if name < collection.val and collection.left:
        collection.left = add_plant(collection.left, name)
    elif name > = collection.val and collection.right:
        collection.right = add_plant(collection.right, name) 
    
        
    return collection"""

"""
            Money Tree
        /              \
Fiddle Leaf Fig    Snake Plant
"""

# Using build_tree() function at the top of page
values = ["Money Tree", "Fiddle Leaf Fig", "Snake Plant", "Aloe"]
collection = build_tree(values)

# Using print_tree() function at the top of page
# print_tree(add_plant(collection, "Aloe"))

# Problem 5

class TreeNode:
    def __init__(self, key, value, left=None, right=None):
        self.key = key      # Plant rarity
        self.val = value      # Plant name
        self.left = left
        self.right = right
# Understand: 
# Input: collections[TreeNode]
# Output: an sorted array [(key, node.val)] -> rank key in increasing order
# Edge cases: empty collections, return empty arr
# Traverse to the left most node, append to the arr as we return, then visit the right node
# The right subtrees gets appended after left subtree

# Plan
# Initialize empty arr
# Inner function: traverse the BST, visit left and right, and inbetween, we append
# Call the inner function in the outer function
# return the arr

# Implement
def sort_plants(collection):
    ans = []
    
    def traverse(node):
        if not node:
            return
        
        traverse(node.left)
        ans.append((node.val, node.key))
        traverse(node.right)
    
    traverse(collection)
    return ans

values = [(3, "Monstera"), (1, "Pothos"), (5, "Witchcraft Orchid"), None, (2, "Spider Plant"), (4, "Hoya Motoskei")]
collection = build_tree(values)

print(sort_plants(collection))







