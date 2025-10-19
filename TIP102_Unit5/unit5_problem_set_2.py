# q4
# u
# want a function that takes in the head and halves each value in ll  and returns new head

# p
# def func
#   set curr to head
#   iterate while curr is not none
#       update the value of the curr to curr / 2
#       set curr to curr next
#   return head

# i
# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# def halve_list(head):
#     curr = head
#     while curr is not None:
#         curr.value = curr.value / 2
#         curr = curr.next
#     return head

# node_one = Node(5)
# node_two = Node(6)
# node_three = Node(7)
# node_one.next = node_two
# node_two.next = node_three

# # Input List: 5 -> 6 -> 7
# print_linked_list(halve_list(node_one))


# q5
# u
# want a function that removes the tail of a linked list and returns the head of the resulting list

# p
# def func
#   set curr to head
#   iterate while curr next is not none
#       set curr to curr next
#   set curr next to None  
#   return head 

# i
# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# def delete_tail(head):
#     curr = head
#     while curr.next.next is not None:
#         curr = curr.next
#     curr.next = None
#     return head


# butterfly = Node("Common Butterfly")
# ladybug = Node("Ladybug")
# beetle = Node("Scarab Beetle")
# butterfly.next = ladybug
# ladybug.next = beetle

# # Input List: butterfly -> ladybug -> beetle
# print_linked_list(delete_tail(butterfly))


# q6
# u
# want a function that takes in the head of a ll and returns the value of the node with min value


# p
# def func
#   set min to head value
#   set curr to head next
#   iterate while curr is not none
#       check if curr value less than min
#           update min to be curr value
#       set curr to curr next
#   return min

# i
# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# def find_min(head):
#     min_value = head.value
#     curr = head.next
#     while curr is not None:
#         if curr.value < min_value:
#             min_value = curr.value
#         curr = curr.next
#     return min_value

# head1 = Node(5, Node(6, Node(7, Node(8))))
# head2 = Node(8, Node(5, Node(6, Node(7))))

# # Linked List: 5 -> 6 -> 7 -> 8
# print(find_min(head1))

# # Linked List: 8 -> 5 -> 6 -> 7
# print(find_min(head2))

# q8
# u
# want a function that takes in the head of a linked list and moves the tail such that it becomes the head and returns this new head

# p
# def func
#   set curr to be head
#   iterate while curr next next is not none
#       set curr to curr next
#   set new head to curr next
#   set curr next to none
#   set new head next head
#   return new head

# i
# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# def tail_to_head(head):
#     curr = head
#     while curr.next.next is not None:
#         curr = curr.next
#     new_head = curr.next
#     curr.next = None
#     new_head.next = head
#     return new_head

# daisy = Node("Daisy")
# mario = Node("Mario")
# toad = Node("Toad") 
# peach = Node("Peach")
# daisy.next = mario
# mario.next = toad
# toad.next = peach

# # Linked List: Daisy -> Mario -> Toad -> Peach
# print_linked_list(tail_to_head(daisy))

# q9
# u
# want to update the Node constructor such that it can be used to create a doubly linked list

# i
# class Node:
#     def __init__(self, value, prev=None, next=None):
#         self.value = value
#         self.prev = prev
#         self.next = next
        
# head = Node("Isabelle")
# tail = Node("K.K Slider")

# head.next = tail
# tail.prev = head

# print(head.value, "<->", head.next.value)
# print(tail.prev.value, "<->", tail.value)

# q10
# u
# want a function that takes in the tail of a doubly linked list and prints the list in reverse with each node separated by a space

# p
# def func
#   set curr to tail
#   set reversed list to ""
#   iterate while curr is not none
#       set reversed list to reversed list + " " + curr value
#       set curr to curr prev
#   return reversed list   

# i
class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

def print_reverse(tail):
    curr = tail
    reversed_list = ""
    while curr is not None:
        reversed_list = reversed_list + " " + curr.value
        curr = curr.prev
    print(reversed_list)

isabelle = Node("Isabelle")
kk_slider = Node("K.K. Slider")
saharah = Node("Saharah")
isabelle.next = kk_slider
kk_slider.next = saharah
saharah.prev = kk_slider
kk_slider.prev = isabelle

# Linked List: Isabelle <-> K.K. Slider <-> Saharah
print_reverse(saharah)


