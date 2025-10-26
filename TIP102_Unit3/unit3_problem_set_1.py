# q1
# u
# want a function that checks a string passed in to verify that there are correct number of opening and closing bracket
# and they are in the correct order

# p
# def func
#   create dictionary match = {')': '(', ']': '[', '}': '{'}
#   create an empty stack
#   iterate through the string
#       check if the elem is an opening bracket
#           if so add to the stack
#           elif check if its a closing bracket
#               if so check if the stack is empty or the last elem is not the value for that bracket in dictionary
#                   return false
#           otherwise
#               pop elem from stack
#       otherwise
#           continue
#   return len of stack equals 0    

# i
def is_valid_post_format(posts):
    match = {')': '(', ']': '[', '}': '{'}
    stack = []

    for ch in posts:
        if ch in '([{':
            stack.append(ch)                       
        elif ch in ')]}':
            if not stack or stack[-1] != match[ch]:
                return False                      
            stack.pop()                           
        else:
         
            continue

    return len(stack) == 0

# print(is_valid_post_format("()"))
# print(is_valid_post_format("()[]{}")) 
# print(is_valid_post_format("(]"))

# q2
# u
# want a function that reverse the order of a list of strings and returns that reversed list using a stack

# p
# def func
#   create empty stack
#   iterate through the array
#       push each elem to the stack
#   create new empty array
#   iterate while stack is not empty
#       append each elem popped from stack into the new array
#   return new array


# i
def reverse_comments_queue(comments):
    new_stack = []
    for each in comments:
        new_stack.append(each)
    new_array = []
    while len(new_stack) > 0:
        new_array.append(new_stack.pop())
    return new_array

# print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

# print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))


# q3
# u
# want a function that checks if a string reads the same from the front and from the back, excluding spaces and non alphanumeric
# case insensitive

# p
# def func
#   create left at 0
#   create right at len(title) - 1
#   iterate while left < right:
#       if elem at right is non alpha:
#           move right pointer inwards
#       elif elem at left is non alpha:
#           move left pointer inwards
#       otherwise both alphanum:
#           check if elem at left lowered not equal elem at right lowered
#               return false
#   return true

# i
def is_symmetrical_title(title):
    left = 0
    right = len(title) - 1
    while left < right:
        if not title[left].isalpha():
            left += 1
        elif not title[right].isalpha():
            right -= 1
        else:
            if title[left].lower() != title[right].lower():
                return False
        left += 1
        right -= 1
    return True

# print(is_symmetrical_title("A Santa at NASA"))
# print(is_symmetrical_title("Social Media")) 

# q4
# u
# want to modify solution so that it uses two pointer technique to square each number in an array and sort

# p

# i
# def engagement_boost(engagements):
#     squared_engagements = []
    
#     # iterate through engagements and square each elem
#     # append the resulting squared number and the index to new array as a tuple
#     for i in range(len(engagements)):
#         squared_engagement = engagements[i] * engagements[i]
#         squared_engagements.append((squared_engagement, i))
    
#     # sorts the list in decreasing order
#     squared_engagements.sort(reverse=True)
    
#     # create result array of zeroes of len engagements
#     # set position to end
#     result = [0] * len(engagements)
#     left = 0
#     right = len(engagements) - 1
    
#     while left <= right:
#         result[left] = squared_engagements[right][0]
#         result[right] = squared_engagements[left][0]
#         left += 1
#         right -= 1
    
#     # position = len(engagements) - 1
    
#     # iterate through array
#     # set elem at position to squared number
#     # decremenet position pointer
#     # for square, original_index in squared_engagements:
#     #     result[position] = square
#     #     position -= 1
    
#     # return result
#     return result

# print(engagement_boost([-4, -1, 0, 3, 10]))
# print(engagement_boost([-7, -3, 2, 3, 11]))

 





