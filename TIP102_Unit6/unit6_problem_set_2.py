# q1
# u
# want a function that takes in head of LL and checks if tail point to head making a cycle

# p
# def func
#   check if head is none
#       if so return false
#   set curr to head
#   iterate while curr is not none
#       check if curr next equals head
#           if so return True
#       set curr to curr next
#   return false

# i
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def is_circular(clues):
    if clues is None:
        return False
    curr = clues
    while curr is not None:
        if curr.next == clues:
            return True
        curr = curr.next
    return False


# clue1 = Node("The stolen goods are at an abandoned warehouse")
# clue2 = Node("The mayor is accepting bribes")
# clue3 = Node("They dumped their disguise in the lake")
# clue1.next = clue2
# clue2.next = clue3
# clue3.next = clue1

# print(is_circular(clue1))

# time: O(n)
# space: O(1)

# q2
# u
# want a function that takes in head of LL and returns an array containing all values that are part of any cycle in the LL, values can be in any order

# p
# def func
#   create seen_array = []
#   set slow to head
#   set fast to head
#   iterate while fast and fast next are not none
#       set slow to slow next
#       set fast to fast next next
#       if slow equals fast
#           break
#   check if when we had to break ie check if slow equals fast
#       add slow value to seen_array
#       set slow to slow next
#       iterate while slow != fast
#           add slow value to seen_array
#           set slow to slow next
#   return seen_array


# i
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def collect_false_evidence(evidence):
    seen_array = []
    slow = evidence
    fast = evidence
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    if slow == fast:
        seen_array.append(slow.value)
        slow = slow.next
        while slow != fast:
            seen_array.append(slow.value)
            slow = slow.next
    return seen_array

# clue1 = Node("Unmarked sedan seen near the crime scene")
# clue2 = Node("The stolen goods are at an abandoned warehouse")
# clue3 = Node("The mayor is accepting bribes")
# clue4 = Node("They dumped their disguise in the lake")
# clue1.next = clue2
# clue2.next = clue3
# clue3.next = clue4
# clue4.next = clue2

# clue5 = Node("A masked figure was seen fleeing the scene")
# clue6 = Node("Footprints lead to the nearby woods")
# clue7 = Node("A broken window was found at the back")
# clue5.next = clue6
# clue6.next = clue7

# print(collect_false_evidence(clue1))
# print(collect_false_evidence(clue5))

# time: O(n)
# space: O(n)

# q3
# u
# want a function that takes in head of LL and an threshold value, then partitions the LL such that nodes with values greater than threshold come before nodes with values
# less than or equal to threshold 

# p
# def func
#   create tempB set to Node(0)
#   set currB = tempB
#   create tempS set to Node(0)
#   set currS = tempS
#   set curr to head of suspect rating
#   iterate while curr is not none
#       check if curr value <= threshold
#           make currS next point to curr
#           set currS to curr
#       otherwise
#           make currB next point to curr
#           set currB to curr
#       set curr to curr next
#   set currB next to tempS next
#   return tempB next

# i
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

def partition(suspect_ratings, threshold):
    tempB = Node(0)
    currB = tempB
    
    tempS = Node(0)
    currS = tempS
    curr = suspect_ratings
    
    while curr is not None:
        if curr.value <= threshold:
            currS.next = curr
            currS = curr
        else:
            currB.next = curr
            currB = curr
        curr = curr.next
    currB.next = tempS.next
    return tempB.next

# suspect_ratings = Node(1, Node(4, Node(3, Node(2, Node(5, Node(2))))))

# print_linked_list(partition(suspect_ratings, 3))

# q4
# u
# want a function that takes in heads of two LL and merges them into one sorted LL byt splicing the nodes from the two LL, return head of sorted LL

# p
# def func
#   create tempHead = Node(0)
#   set tempCurr = tempHead
#   set curr_known = head known
#   set curr_witness = head_witness
#   iterate while curr_known and curr_witness both not none
#       check if curr_known <= curr_witness
#           if so set tempCurr next to curr_known 
#           set tempCurr to curr_known
#           set curr_known to curr_known next
#       otherwise
#           set tempCurr next to curr_witness
#           set tempCurr to curr_witness
#           set curr_witness to curr_witness next
#   if curr_known and not curr_witness
#       set tempCurr next to curr_known
#   elif curr_witness and not curr_known
#       set tempCurr next to curr_witness
#   return tempHead next

# i
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def merge_timelines(known_timeline, witness_timeline):
    tempHead = Node(0)
    tempCurr = tempHead
    curr_known = known_timeline
    curr_witness = witness_timeline
    while curr_known and curr_witness:
        if curr_known.value <= curr_witness.value:
            tempCurr.next = curr_known
            tempCurr = curr_known
            curr_known = curr_known.next
        else:
            tempCurr.next = curr_witness
            tempCurr = curr_witness
            curr_witness = curr_witness.next
    if curr_known and not curr_witness:
        tempCurr.next = curr_known
    elif curr_witness and not curr_known:
        tempCurr.next = curr_witness
    return tempHead.next

known_timeline = Node(1, Node(2, Node(4)))
witness_timeline = Node(1, Node(3, Node(4)))

print_linked_list(merge_timelines(known_timeline, witness_timeline))
 