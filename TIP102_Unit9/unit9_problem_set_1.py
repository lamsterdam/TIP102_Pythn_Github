# UPI

# Problem 1

# Understanding:
# Given two trees, merge it into one tree
# For nodes in the same values at both of the given trees, sums the values
# Otherwise, if there is only one node that exists at a position, uses the non-empty node of one of the trees

# Planning:
# if both trees are empty, 
#   return None
# if one of the trees is empty and the other is non-empty, 
#   return the non-empty tree
# if both of the trees are non-empty, 
#   create a new TreeNode where the value is the sum the values of the root nodes of the two trees
# left of the new TreeNode -> call function on left trees of both trees
# right of the new TreeNode -> call function on right trees of both trees

# Implementation

from collections import deque 

# Tree Node class
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

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

from collections import deque 

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

def merge_orders(order1, order2):
    if not order1 and not order2:
        return None
    if not order1 and order2:
        return order2
    if order1 and not order2:
        return order1
    
    new_tree = TreeNode(order1.val + order2.val)
    # new_tree.val = order1.val + order2.val
    new_tree.left = merge_orders(order1.left, order2.left)
    new_tree.right = merge_orders(order1.right, order2.right)

    return new_tree

"""
     1             2         
    /  \         /   \       
   3    2       1     3   
 /               \      \   
5                 4      7   
"""
# Using build_tree() function included at top of page
cookies1 = [1, 3, 2, 5]
cookies2 = [2, 1, 3, None, 4, None, 7]
order1 = build_tree(cookies1)
order2 = build_tree(cookies2)

# Using print_tree() function included at top of page
# print_tree(merge_orders(order1, order2))



# Problem 2

# UPI

# Understanding
# taking in root of a tree print the bfs traversal of the tree

# Planning
# create a list for the result and set that to be empty
# if the tree is empty,
#    return an empty list
# create an empty queue
# add the root into the queue
# use while loop for while queue is not empty
#   pop left off queue
#   add popped to list
#   add popped left to queue
#   add popped right to queue
# return list


# Implementation

class Puff():
     def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right

def print_design(design):
    result = []
    if not design:
        return []
    bfs_queue = deque()
    bfs_queue.append(design)
    
    while bfs_queue:
        popped_elem = bfs_queue.popleft()
        result.append(popped_elem.val)
        if popped_elem.left:
            bfs_queue.append(popped_elem.left)
        if popped_elem.right:
            bfs_queue.append(popped_elem.right)
    return result


"""
            Vanilla
           /       \
      Chocolate   Strawberry
      /     \
  Vanilla   Matcha  
"""
croquembouche = Puff("Vanilla", 
                    Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")), 
                    Puff("Strawberry"))
print(print_design(croquembouche))


# Problem 3

# UPI

# Understanding
# Given a tree, return the maxinum number of tiers in cake = number of nodes along the longest path from the root node down to the farthest leaf node



# Planning
# if not root,
#   return 0
# otherwise if root is not empty,
#   return 1 + max(max_tiers(cake.left), max_tiers(cake.right))


# Implementation
class TreeNode():
     def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def max_tiers(cake):
    if not cake:
        return 0
    return 1 + max(max_tiers(cake.left), max_tiers(cake.right))

"""
        Chocolate
        /        \
    Vanilla    Strawberry
                /     \
         Chocolate    Coffee
"""
# Using build_tree() function included at top of page
cake_sections = ["Chocolate", "Vanilla", "Strawberry", None, None, "Chocolate", "Coffee"]
cake = build_tree(cake_sections)

print(max_tiers(cake))