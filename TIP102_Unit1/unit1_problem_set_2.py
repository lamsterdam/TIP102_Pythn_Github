"""
Problem 1: Reverse Sentence
Write a function reverse_sentence() that takes in a string sentence and 
returns the sentence with the order of the words reversed. The sentence will 
contain only alphabetic characters and spaces to separate the words. 
If there is only one word in the sentence, the function should return the original string.

def reverse_sentence(sentence):
    pass
Example Usage:

sentence = "tubby little cubby all stuffed with fluff"
reverse_sentence(sentence)

sentence = "Pooh"
reverse_sentence(sentence)
Example Output:

"fluff with stuffed all cubby little tubby"
"Pooh"
"""
# Understand:
# reversing an entire string
# if it's one word, just returning the original string 
# edge case: if empty string return that string 

# Plan:
# create an empty string called reverse_str
# find the length of the string
# loop over the string
# if element exist, add to the reverse_str
# once done looping return reverse_str

# def reverse_sentence(sentence):
#     # create an empty string called reverse_str
#     reverse_str = ""
#     new_str = sentence.split()
#     # print(new_str)
#     str_len = len(new_str)
#     # loop over the string
#     for word in range(str_len-1, -1, -1):
#         # add to the reverse_str
#         reverse_str += new_str[word] + " "    
#     # once done looping return reverse_str
#     return reverse_str


sentence = "tubby little cubby all stuffed with fluff"
# print(reverse_sentence(sentence))

sentence = "Pooh"
# print(reverse_sentence(sentence))


"""
Problem 2: Goldilocks Number
In the extended universe of fictional bears, Goldilocks finds an 
enticing list of numbers in the Three Bears' house. She doesn't want 
to take a number that's too high or too low - she wants a number that's 
juuust right. Write a function goldilocks_approved() that takes in the list of 
distinct positive integers nums and returns any number from the list that is
neither the minimum nor the maximum value in the array, or -1 if there is no such number.
Return the selected integer.

def goldilocks_approved(nums):
    pass
Example Usage

nums = [3, 2, 1, 4]
goldilocks_approved(nums)

nums = [1, 2]
goldilocks_approved(nums)

nums = [2, 1, 3]
goldilocks_approved(nums)
Example Output:
2
-1
2
"""

# u
# want a function that checks the numbers in an array, and returns a number that is neither the max 
# nor the min. if there is no number that is neither max nor min return -1

# p
# def func
#   check if length of list is 2 or less
#       return -1
#   otherwise 
#       sort the list
#       get the elem at second position
#   return that elem

# i
# def goldilocks_approved(nums):
#     if len(nums) <= 2:
#         return -1
#     else:
#         nums.sort()
#         chosen_elem = nums[1]
#     return chosen_elem

# nums = [3, 2, 1, 4]
# print(goldilocks_approved(nums))

# nums = [1, 2]
# print(goldilocks_approved(nums))

# nums = [2, 1, 3]
# print(goldilocks_approved(nums))

"""
Pooh is eating all of his hunny jars in order of smallest to largest. 
Given a list of integers hunny_jar_sizes, write a function delete_minimum_elements() 
that continuously removes the minimum element until the list is empty. Return a 
new list of the elements of hunny_jar_sizes in the order in which they were removed.

def delete_minimum_elements(hunny_jar_sizes):
	pass
Example Usage

hunny_jar_sizes = [5, 3, 2, 4, 1]
delete_minimum_elements(hunny_jar_sizes)

hunny_jar_sizes = [5, 2, 1, 8, 2]
delete_minimum_elements(hunny_jar_sizes)
Example Output:

[1, 2, 3, 4, 5]
[1, 2, 2, 5, 8]
"""

# u
# want a function that continuously removes the minimum elem from a list until it is empty, and retuns a new list of the elements in the order they were removed

# p
# def func:
#   create new empty list 
#   iterate while list is not empty
#      find the minimum 
#       add this elem to new list 
#       remove elem from list
#   return new list

# i
# def delete_minimum_elements(hunny_jar_sizes):
#     newList = []
#     while len(hunny_jar_sizes) > 0:
#         min_elem = min(hunny_jar_sizes)
#         newList.append(min_elem)
#         hunny_jar_sizes.remove(min_elem)
#     return newList

# hunny_jar_sizes = [5, 3, 2, 4, 1]
# print(delete_minimum_elements(hunny_jar_sizes))

# hunny_jar_sizes = [5, 2, 1, 8, 2]
# print(delete_minimum_elements(hunny_jar_sizes))

# q4
# u
# want a function that takes in an integer and returns the sum of the digits in that integer

# p
# def func
#   convert the int to a string
#   split the string between each digit
#   set sum_value to 0
#   iterate over the digit list
#       on each pass add the elem to sum_value
#   return sum_value

# i
def sum_of_digits(num):
    pass