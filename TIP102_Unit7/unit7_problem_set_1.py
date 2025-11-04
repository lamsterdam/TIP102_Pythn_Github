# q1
# p
# def func:
#   set count = 0
#   iterate through suits
#       increment count
#   return count
def count_suits_iterative(suits):
    count = 0
    
    for s in suits:
        count +=1
    return count


# if no suits -> return 0
# if index[i] > or = len(suits - 1) -> return 0
# return 1 + count_suits_recursive(suits[1:])

def count_suits_recursive(suits):
    if not suits:
        return 0
    #if index[i] > len(suits -1):
     #   return 0
    return 1 + count_suits_recursive(suits[1:])
                                           
# print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
# print(count_suits_recursive(["Mark I", "Mark II", "Mark III"]))

# a = ["Mark I", "Mark II", "Mark III"]= 1 + b = 1 + 2 = 3
# b = (["Mark II", "Mark III"]) = 1 + c = 1 + 1 = 2
# c = ["Mark III"] = 1 + d 1 + 0 = 1
# d = [] = 0

#######################################################################################################
# q2
# u
# want a function that takes in an array of stones and return the total power

# p
# def func
#   base case:
#   check if index is == len array
#       return 0
#   recursive case:
#   return elem at i + func(array[i+1])

# i
def sum_stones(stones, index):
    if index == len(stones):
        return 0
    return stones[index] + sum_stones(stones, index+1)

# print(sum_stones([5, 10, 15, 20, 25, 30], 0))
# print(sum_stones([12, 8, 22, 16, 10], 0))

# Time: O(n)
# Space: O(n), each recursive call is added to call stack, n elements so n recursive calls

#######################################################################################################
# q3
# u 
# want functions iteratively and recursively to count distint suits in the list

# p
# def func
#   create an empty set
#   iterate through array
#       add each element to the set
#   return length of the set

# p recurse
# def func
#   base case:
#   check if array is empty
#       return 0
#   recursive case:
#   get the first elem from array
#   get the rest of array arr[1:]
#   check if the first elem is in the rest of array
#       return recursive call on rest of array
#   otherwise
#       retur 1 + recursive call on rest of array

# i
def count_suits_iterative(suits):
    new_set = set()
    for each in suits:
        new_set.add(each)
    return len(new_set)

# Time: O(n)
# Space: O(n)

def count_suits_recursive(suits):
    if len(suits) == 0:
        return 0
    first_elem = suits[0] # O(1)
    rest_array = suits[1:] # O(n)
    if first_elem in rest_array:
        return count_suits_recursive(rest_array) # O(n)
    else:
        return 1 + count_suits_recursive(rest_array)

# print(count_suits_iterative(["Mark I", "Mark I", "Mark III"]))
# print(count_suits_recursive(["Mark I", "Mark I", "Mark III"]))

# Time: O(n^2), each recursive call does O(n) work and we call the function n times
# Space: O(n^2)

#######################################################################################################
# q4