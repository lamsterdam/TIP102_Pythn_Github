# ask questions like if its a string, what if its empty, can there be numbers or just letters, only alphanum?
# if its a list what if the list is empty, what if there are duplicate elements, do we care if the list is sorted?
# always try to constrain the problem down, but dont over ask and spend like 10 mins on just asking, try to do like 5 mins max

# q1
# u
# want a function that prints the desired message

# p
# def func:
#   print("Welcome to The Hundred Acre Wood!")

# i
# def welcome():
# 	print("Welcom to the Hundred Ace Wood!")
 
# result = welcome()
# print(result)

# q2
# want a function that prints the desired message with the name passed in

# def func:
#   print("the message") using that f string

# i
# def greeting(name):
# 	print(f"Welcome to The Hundred Acre Wood {name}! My name is Christopher Robin.")

# result = greeting("Michael")

# q3
# want a function that prints out a catchphrase based on the char name, if not listed name print other message

# p
# def func:
#   check if name is pooh:
#       if so print pooh messag
#   elif check if name is tigger:
#       if so print tigger msg
#   elif check eyeyore
#       print eyeore msg
#   elif chis
#       print chris msg
#   else:
#       print the sorry one

# i
# def print_catchphrase(character):
#     if character == "Pooh":
#         print("Oh bother!")
#     elif character == "Tigger":
#         print("TTFN: Ta-ta for now!")
#     elif character == "Eeyore":
#         print("Thanks for noticing me.")
#     elif character == "Christopher Robin":
#         print("Silly old bear.")
#     else:
#         print(f"Sorry! I don't know {character}'s catchphrase!")

# character = "Piglet"
# print_catchphrase(character)

# q4
# u
# want a function that takes in alist and an index and returns the elem at the index, if index not valid return None

# p
# def func:
#   get the length of the list
#   check if index is greater than length - 1
#       return None
#   otherwise
#       return elem at that index

# i
# def get_item(items, x):
#     if x > len(items) - 1:
#         return None
#     elif x < 0:
#         return None
#     return items[x]

# items = ["piglet", "pooh", "roo", "rabbit"]
# x = -1
# result = get_item(items, x)
# print(result)

# q5
# u
# want a function that sums up all integers in list without using built in sum

# p
# def func
#   create total var set to 0
#   iterate through the list
#       add the elem to total
#   return total

# i
# def sum_honey(hunny_jars):
#     total = 0
#     for each in hunny_jars:
#         total += each
#     return total

# hunny_jars = []
# result = sum_honey(hunny_jars)
# print(result)

# q6
# u
# want a function that multiplies each elem in list by two and returns the doubled list

# p
# def func
#   iterate through the list
#       multiply each elem by 2
#   return list

# i
def doubled(hunny_jars):
    for i in range(len(hunny_jars)):
        hunny_jars[i] *= 2 
    return hunny_jars

hunny_jars = [1, 2, 3]
print(doubled(hunny_jars))
     
 
     

    
