from collections import deque 

# Tree Node class
class TreeNode:
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

##############################################################################
# q1
# want to build the tree

# i
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right
        
root = TreeNode("Trunk")
mcintosh = TreeNode("Mcintosh")
granny_smith = TreeNode("Granny Smith")
fuji = TreeNode("Fuji")
opal = TreeNode("Opal")
crab = TreeNode("Crab")
gala = TreeNode("Gala")

root.left = mcintosh
root.right = granny_smith

mcintosh.left = fuji
mcintosh.right = opal

granny_smith.left = crab
granny_smith.right = gala

# Using print_tree() included at the top of this page
# print_tree(root)

##############################################################################
# q2
# want a func to take in root of tree which is a mathematical operator and return the 
# result when applied to the leaves

# p
# def func
#   check if root val is +
#       return left child + right
#   elif check if root val is -
#       return left child - right
#   elif check if root val is *
#       return left child * right
#   otherwise
#       return left child / right


# i
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def calculate_yield(root):
    if root.val == "+":
        return root.left.val + root.right.val
    elif root.val == "-":
        return root.left.val - root.right.val
    elif root.val == "*":
        return root.left.val * root.right.val
    else:
        return root.left.val / root.right.val

"""
    +
  /   \
 7     5
"""
apple_tree = TreeNode("+", TreeNode(7), TreeNode(5))

# print(calculate_yield(apple_tree))

##############################################################################
# q3
# want a func to take in root and return a list of nodes in path root to right most node
# so all the right children in right subtree until that node

# p
# def func
#   check if root is none
#       return 
#   return [root.val] + func(root.right)

# i
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def right_vine(root):
    if root is None:
        return []
    return [root.val] + right_vine(root.right) 

"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""
ivy1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

"""
      Root
      /  
    Node1
    /
  Leaf1  
"""
ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

# print(right_vine(ivy1))
# print(right_vine(ivy2))

##############################################################################
# q4
# u 
# want to implement prev question iteratively

# p
# def func
#   create empty list
#   check if root is None
#       return empty list
#   set curr to root
#   iterate while curr is not None
#       add curr value to list
#       set curr to curr right
#   return list

# i
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def right_vine(root):
    vine_cutting = []
    if root is None:
        return []
    current_node = root
    while current_node is not None:
        vine_cutting.append(current_node.val)
        current_node = current_node.right
    return vine_cutting

"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""
ivy1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

"""
      Root
      /  
    Node1
    /
  Leaf1  
"""
ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

# print(right_vine(ivy1))
# print(right_vine(ivy2))

##############################################################################
# q5
# u
# want a function that counts the number of leaves in a binary tree, aka the ones with no children and return that count

# p 
# def func
#   check if root is none
#       return 0
#   check if no root root right and no root left
#       return 1
#   set left leaves to func(root left)
#   set right leaves to func(root right)
#   return left leaves + right leaves

# i
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def count_leaves(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    left_leaves = count_leaves(root.left)
    right_leaves = count_leaves(root.right)
    return left_leaves + right_leaves

"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""

oak1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

"""
      Root
      /  
    Node1
    /
  Leaf1  
"""
oak2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))


print(count_leaves(oak1))
print(count_leaves(oak2))
