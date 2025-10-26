# q2
# u
# want a function that checks the words in an array and retruns the name of the first
# palindrome, if none exist we return empty string

# p
# def func
#   iterate through the array
#       left equal to 0
#       right equal to len of elem -1
#       iterate while left less than right
#           check if elem at left not equals elem at right
#               break
#           otherwise
#               increment left
#               decrement right
#       return this elem
#   return ""

# i
def first_symmetrical_landmark(landmarks):
    for each in landmarks:
        left = 0
        right = len(each) - 1
        while left < right:
            if each[left] != each[right]:
                break
            else:
                left += 1
                right -=1
        if left >= right:
            return each
    return ""

# print(first_symmetrical_landmark(["canyon","forest","rotor","mountain"])) 
# print(first_symmetrical_landmark(["plateau","valley","cliff"])) 

# q3
# u
# given a string of I's and D's where I means its less than the next elem and D means its bigger than the next elem, reconstrcut
# the string into an array of integers

# p
# def func
#   set smallest available number to 0
#   set largest available number to len(string)
#   create empty array
#   iterate through string
#       check if elem is I
#           if so set elem in array at that index to smallest avail
#           increase smallest avail
#       otherwise
#           elem is D so set elem in array at that index to largest avail
#           decrease largest avail
#   theres an extra append low
#   return array


# i
def terrain_elevation_match(terrain):
    smallest_avail = 0
    largest_avail = len(terrain)
    new_array = []
    for i in range(len(terrain)):
        if terrain[i] == "I":
            new_array.append(smallest_avail)
            smallest_avail += 1
        else:
            new_array.append(largest_avail)
            largest_avail -= 1
    new_array.append(smallest_avail)
    return new_array

# print(terrain_elevation_match("IDID")) 
# print(terrain_elevation_match("III")) 
# print(terrain_elevation_match("DDI")) 

# q4
# u
# want a function that takes in an array of numbers and concatenates them based on certain criteria and returns the result

# p
# def func
#   set left euqla to 0
#   set right equal to len of array - 1
#   set concat val = 0
#   iterate while left <= right
#       check if left equals right
#           if so set new num equal to elem at left
#           update concate val to be concat val + new num
#       set new num equal to elem at left + elem at right
#       update concate val to be concat val + new num
#       increment left
#       decreement right
#   return concat val

# i
def find_the_log_conc_val(logs):
    left = 0
    right = len(logs) - 1
    concat_val = 0
    while left <= right:
        if left != right:
            new_num = int(str(logs[left]) + str(logs[right]))
            concat_val += new_num
        else:
            new_num = logs[left]
            concat_val += new_num
        left += 1
        right -= 1
    return concat_val

# print(find_the_log_conc_val([7, 52, 2, 4])) 
# print(find_the_log_conc_val([5, 14, 13, 8, 12])) 

# q5
# u
# explorers = [1,1,0,0] supplies = [0,1,0,1]
# explorers = [1,0,0,1] supplies = [0,1,0,1]
# explorers = [0,0,1,1] supplies = [0,1,0,1] 0 will take 0 and leave queue and pop from stack
# explorers = [1,1,0] supplies = [1,0,1]
# explorers = [1,0] supplies = [0,1] 1 will take 1 and leave queue and pop from stack
# explorers = [0,1] supplies = [0,1]
# explorers = [1] supplies = [1] 0 will take 0 and leave queue and pop from stack
# explorers = [] supplies = [] 1 will take 1 and leave queue and pop from stack, the explorers is empty

# explorers = [1, 1, 1, 0, 0, 1] supplies = [1, 0, 0, 0, 1, 1] 1 will take 1 and leave queue and pop from stack
# explorers = [1, 1, 0, 0, 1] supplies = [0, 0, 0, 1, 1]
# explorers = [1, 0, 0, 1, 1] supplies = [0, 0, 0, 1, 1]
# explorers = [0, 0, 1, 1, 1] supplies = [0, 0, 0, 1, 1] 0 will take 0 and leave queue and pop from stack
# explorers = [0, 1, 1, 1] supplies = [0, 0, 1, 1] 0 will take 0 and leave queue and pop from stack
# explorers = [1, 1, 1] supplies = [0, 1, 1]
# explorers = [1, 1, 1] supplies = [0, 1, 1] the 1,1,1 will jsut shuffle around and we will never get the 0 supply popped so ending is when the elem at top of stack is 
# not in queue

# so want a function that checks the elem at front of queue to see is equal to elem at top of stack, if they are euqal remove from queue and pop top from stack
# otherwise move elem at front of queue to back of queue and check again. When the elem at top of stack cannot be found in queue return the length of the queue

# p
# def func
#   create an empty queue
#   iterate through explorers array
#       append each elem to the queue
#   iterate while elem at top of stack which is 0th elem in this case is not in queue and stack is not empty
#       check if elem at front of queue equals elem at top of stack
#           if so remove elem from queue and remove elem from stack
#       otherwise
#           remove elem from queue and append it to the back
#   return length of queue


# i
from collections import deque
def count_explorers(explorers, supplies):
    myQueue = deque()
    for each in explorers:
        myQueue.append(each)
    while supplies and supplies[0] in myQueue:
        top_queue = myQueue.popleft()
        print(f"top pf queue {top_queue}")
        if top_queue == supplies[0]:
            top_stack = supplies.pop(0)
            print(f"top of stack {top_stack}")
        else:
            myQueue.append(top_queue)
    return len(myQueue)

# print(count_explorers([1, 1, 0, 0], [0, 1, 0, 1]))  
# print(count_explorers([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1])) 

# q6
# u
# 