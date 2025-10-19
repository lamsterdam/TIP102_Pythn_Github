# q1
# u
# want  to copy the code and create an instance of it

# class Villager:
#     def __init__(self, name, species, catchphrase):
#         self.name = name
#         self.species = species
#         self.catchphrase = catchphrase
#         self.furniture = []

# # Instantiate your villager here
# apollo = Villager("Apollo", "Eagle", "pah")

# print(apollo.name)  
# print(apollo.species)  
# print(apollo.catchphrase) 
# print(apollo.furniture) 

# q2
# u
# want to reuse village class, create a new instance and add a greet player method that displays the message

# i
# class Villager:
#     def __init__(self, name, species, catchphrase):
#         self.name = name
#         self.species = species
#         self.catchphrase = catchphrase
#         self.furniture = []
        
#     def greet_player(self, player_name):
#         return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"

# bones = Villager("Bones", "Dog", "yip yip")
# print(bones.greet_player("Leigh"))

# q3
# u
# want to edit the 3rd param in constructor

# i
# class Villager:
#     def __init__(self, name, species, catchphrase):
#         self.name = name
#         self.species = species
#         self.catchphrase = catchphrase
#         self.furniture = []
        
#     def greet_player(self, player_name):
#         return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"

# bones = Villager("Bones", "Dog", "ruff it up")
# print(bones.greet_player("Leigh"))


# q4
# u
# want to add a setter method to update the villagers catch phrase and check validity

# i
# class Villager:
#     def __init__(self, name, species, catchphrase):
#         self.name = name
#         self.species = species
#         self.catchphrase = catchphrase
#         self.furniture = []
        
#     def greet_player(self, player_name):
#         return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"
    
#     def set_catchphrase(self, new_catchphrase):
#         # set stripped catchphrase to new catch phrase stripped of whitespace
#         # check if catchphrase has length less than 20 and stripped only contains alpha char
#         #   set the catchphrase to new catchphrase
#         #  otherwise
#         #   print invalid catchphrase
#         stripped_catchphrase = ''.join(ch for ch in new_catchphrase if not ch.isspace())
#         # print(stripped_catchphrase)
#         if len(new_catchphrase) < 20 and stripped_catchphrase.isalpha():
#             self.catchphrase = new_catchphrase
#             print("Catchphrase updated")
#             # print(self.catchphrase)
#         else:
#             print("Invalid catchphrase")

# alice = Villager("Alice", "Koala", "guvnor")

# alice.set_catchphrase("sweet dreams")
# print(alice.catchphrase)
# alice.set_catchphrase("#?!")
# print(alice.catchphrase)

# q5
# u
# want to add amethod to the class to update the item name attribute and validate

# i
# class Villager:
#     def __init__(self, name, species, catchphrase):
#         self.name = name
#         self.species = species
#         self.catchphrase = catchphrase
#         self.furniture = []
        
#     def greet_player(self, player_name):
#         return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"
    
#     def set_catchphrase(self, new_catchphrase):
#         # set stripped catchphrase to new catch phrase stripped of whitespace
#         # check if catchphrase has length less than 20 and stripped only contains alpha char
#         #   set the catchphrase to new catchphrase
#         #  otherwise
#         #   print invalid catchphrase
#         stripped_catchphrase = ''.join(ch for ch in new_catchphrase if not ch.isspace())
#         # print(stripped_catchphrase)
#         if len(new_catchphrase) < 20 and stripped_catchphrase.isalpha():
#             self.catchphrase = new_catchphrase
#             print("Catchphrase updated")
#             # print(self.catchphrase)
#         else:
#             print("Invalid catchphrase")
    
#     # New method
#     def add_item(self, item_name):
#         # check if item name equals any of the valid strings
#         #   if so add it to the furnititure attribute
#         if (item_name == "acoustic guitar" or item_name == "ironwood kitchenette" 
#             or item_name == "rattan armchair" or item_name == "kotatsu" or item_name == "cacao tree"):
#             self.furniture.append(item_name)

# alice = Villager("Alice", "Koala", "guvnor")
# print(alice.furniture)

# alice.add_item("acoustic guitar")
# print(alice.furniture)

# alice.add_item("cacao tree")
# print(alice.furniture)

# alice.add_item("nintendo switch")
# print(alice.furniture)

# q6 and q7

# i
# class Villager:
#     def __init__(self, name, species, personality, catchphrase):
#         self.name = name
#         self.species = species
#         self.personality = personality
#         self.catchphrase = catchphrase
#         self.furniture = []
        
#     def greet_player(self, player_name):
#         return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"
    
#     def set_catchphrase(self, new_catchphrase):
#         # set stripped catchphrase to new catch phrase stripped of whitespace
#         # check if catchphrase has length less than 20 and stripped only contains alpha char
#         #   set the catchphrase to new catchphrase
#         #  otherwise
#         #   print invalid catchphrase
#         stripped_catchphrase = ''.join(ch for ch in new_catchphrase if not ch.isspace())
#         if len(new_catchphrase) < 20 and stripped_catchphrase.isalpha():
#             self.catchphrase = new_catchphrase
#             print("Catchphrase updated")
#             # print(self.catchphrase)
#         else:
#             print("Invalid catchphrase")
    
#     # New method
#     def add_item(self, item_name):
#         # check if item name equals any of the valid strings
#         #   if so add it to the furnititure attribute
#         if (item_name == "acoustic guitar" or item_name == "ironwood kitchenette" 
#             or item_name == "rattan armchair" or item_name == "kotatsu" or item_name == "cacao tree"):
#             self.furniture.append(item_name)
    
#     def print_inventory(self):
#         # check if fuurniture list is empty
#         #   if so print inventory empty
#         # create empty dictionary
#         # iterate through the furniture list
#         #   check if item in dict
#         #       if so increment count
#         #   otherwise
#         #       set value to 1
#         #   print the dictionary
#         if len(self.furniture) == 0:
#             print("Inventory empty")
#         new_dict = {}
#         for each in self.furniture:
#             if each in new_dict:
#                 new_dict[each] += 1
#             else:
#                 new_dict[each] = 1
#         print(new_dict)
    
        
# def of_personality_type(townies, personality_type):
#     # create empty list
#     # check the villages in the townies list to see if their personality matches input
#     #   if so add to list
#     # return list
#     my_list = []
#     for each in townies:
#         if each.personality == personality_type:
#             my_list.append(each.name)
#     return my_list

# isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
# bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
# stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")

# print(of_personality_type([isabelle, bob, stitches], "Lazy"))
# print(of_personality_type([isabelle, bob, stitches], "Cranky"))

# q8
# u
# want a function that takes in two neighbours and returns True if you can pass a message from neighbour 1 to neighbour 2 and False otherwise


# p
# def func
#   check if start villager neighbour is None
#       if so return False
#   check if start villager neighbour is target neighbour
#       if so return True
#   set curr to start villager
#   iterate while curr neighbour is not None
#       check if start neighbour is target neighbour
#           if so return True
#       otherwise
#           set curr to curr neighbour
#   return False

# i
# class Villager:
#     def __init__(self, name, species, personality, catchphrase, neighbor=None):
#         self.name = name
#         self.species = species
#         self.personality = personality
#         self.catchphrase = catchphrase
#         self.furniture = []
#         self.neighbor = neighbor
#     # ... methods from previous problems
    
# def message_received(start_villager, target_villager):
#     if start_villager.neighbor is None:
#         return False
#     curr = start_villager
#     while curr.neighbor is not None:
#         if curr.neighbor == target_villager:
#             return True
#         else:
#             curr = curr.neighbor
#     return False

# isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
# tom_nook = Villager("Tom Nook", "Raccoon", "Cranky", "yes, yes")
# kk_slider = Villager("K.K. Slider", "Dog", "Lazy", "dig it")
# isabelle.neighbor = tom_nook
# tom_nook.neighbor = kk_slider

# print(message_received(isabelle, kk_slider))
# print(message_received(kk_slider, isabelle))

# q9 & q10 & q11
# u 
# want a function that creates a linked list with the values provided

# i
# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# tom_nook = Node("Tom Nook")
# tommy = Node("Tommy")
# timmy = Node("Timmy")
# tom_nook.next = timmy
# timmy.next = tommy

# print(tom_nook.value)
# print(tom_nook.next.value)

# print(timmy.value)
# print(timmy.next.value)

# print(tommy.value)
# print(tommy.next)

# tommy = Node("Tommy")
# timmy = Node("Timmy")
# saharah = Node("Saharah")
# timmy.next = tommy
# tommy.next = saharah

# print(timmy.value)
# print(timmy.next.value)

# print(tommy.value)
# print(tommy.next.value)

# print(saharah.value)
# print(saharah.next)

# q12
# u
# want a function that takes in a head and return the linked list as a string with each node separated by an arro ->

# p
# def func
#   set curr to head
#   set ll_string = ""
#   iterate while curr is not None
#       append "->" + curr value to ll_string
#       set curr to curr next
#   return ll_string

# i
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
def print_list(head):
    ll_string = ""
    ll_string = ll_string + head.value
    curr = head.next
    while curr is not None:
        ll_string = ll_string + "->" + curr.value
        curr = curr.next
    return ll_string

isabelle = Node("Isabelle")
saharah = Node("Saharah")
cj = Node("C.J.")

isabelle.next = saharah
saharah.next = cj

print(print_list(isabelle))
