# q1
# want a function to take in a top_hits_2010s which is a linked list and printing the list

# i
# class SongNode:
#     def __init__(self, song, next=None):
#         self.song = song
#         self.next = next

# # For testing
# def print_linked_list(node):
#     current = node
#     while current:
#         print(current.song, end=" -> " if current.next else "")
#         current = current.next
#     print()
        
# #top_hits_2010s = SongNode("Uptown Funk", SongNode("Party Rock Anthem", SongNode("Bad Romance")))
# uptown = SongNode("Uptown Funk")
# party = SongNode("Party Rock Anthem")
# romance = SongNode("Bad Romance")
# uptown.next = party
# party.next = romance
# print_linked_list(uptown)

# q2
# want a function that takes in a linked list and creates a dictionary of each artist and 
# count in the list

# p
# def func
#   create dictionary
#   set curr to head
#   iterate while curr is not none
#       check if curr.artist in dict
#           if so increment count
#       otherwise
#           add to dict
#   return dict

# i
# class SongNode:
#     def __init__(self, song, artist, next=None):
#         self.song = song
#         self.artist = artist
#         self.next = next

# # For testing
# def print_linked_list(node):
#     current = node
#     while current:
#         print((current.song, current.artist), end=" -> " if current.next else "")
#         current = current.next
#     print()


def get_artist_frequency(playlist):
    new_dict = {}
    curr = playlist
    while curr:
        if curr.artist in new_dict:
            new_dict[curr.artist] += 1
        else:
            new_dict[curr.artist] = 1
        curr = curr.next
    return new_dict

# playlist = SongNode("Saturn", "SZA", 
#                 SongNode("Who", "Jimin", 
#                         SongNode("Espresso", "Sabrina Carpenter", 
#                                 SongNode("Snooze", "SZA"))))

# print(get_artist_frequency(playlist))

#q3

# class SongNode:
#     def __init__(self, song, artist, next=None):
#         self.song = song
#         self.artist = artist
#         self.next = next
        
# # For testing
# def print_linked_list(node):
#     current = node
#     while current:
#         print((current.song, current.artist), end=" -> " if current.next else "")
#         current = current.next
#     print()


# # Function with a bug!
def remove_song(playlist_head, song):
    if not playlist_head:
        return None
    if playlist_head.song == song:
        return playlist_head.next

    current = playlist_head
    while current.next:
        if current.next.song == song:
            current.next = current.next.next  
            return playlist_head 
        current = current.next

    return playlist_head

# playlist = SongNode("SOS", "ABBA", 
#                 SongNode("Simple Twist of Fate", "Bob Dylan",
#                     SongNode("Dreams", "Fleetwood Mac",
#                         SongNode("Lovely Day", "Bill Withers"))))

# print_linked_list(remove_song(playlist, "Dreams"))

#q4
# u
# want to check if a linked list has a cycle

# p
# def func
#   set slow to head
#   set fast to head
#   iterate while fast and fast next
#       set slow to slow next
#       set fast to fast next next
#   check if slow equals head
#       if so return True
#   return Fast

# i
# class SongNode:
#     def __init__(self, song, artist, next=None):
#         self.song = song
#         self.artist = artist
#         self.next = next

def on_repeat(playlist_head):
    slow = playlist_head
    fast = playlist_head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# song1 = SongNode("GO!", "Common")
# song2 = SongNode("N95", "Kendrick Lamar")
# song3 = SongNode("WIN", "Jay Rock")
# song4 = SongNode("ATM", "J. Cole")
# song1.next = song2
# song2.next = song3
# song3.next = song4
# song4.next = song2

# print(on_repeat(song1))

#q5
# u
# want a function that check if there is a cycle and return the length otherwise return 0

# p
# def func
#   set count = 0
#   check for cycle
#   set slow to head
#   set fast to head
#   iterate while fast and fast next
#       set slow to slow next
#       set fast to fast next next
#   check if slow equals fast
#       set count = 1
#       while slow != fast
#           slow = slow next
#           increment count
#   return count

# i
# class SongNode:
#     def __init__(self, song, artist, next=None):
#         self.song = song
#         self.artist = artist
#         self.next = next

# For testing
# def print_linked_list(node):
#     current = node
#     while current:
#         print((current.song, current.artist), end=" -> " if current.next else "")
#         current = current.next
#     print()

def loop_length(playlist_head):
    count = 0
    slow = playlist_head
    fast = playlist_head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            count = 1
            slow = slow.next
            while slow != fast:
                slow = slow.next
                count += 1
            return count     
    return count

# song1 = SongNode("Wein", "AL SHAMI")
# song2 = SongNode("Si Ai", "Tayna")
# song3 = SongNode("Qalbi", "Yasser Abd Alwahab")
# song4 = SongNode("La", "DYSTINCT")
# song1.next = song2
# song2.next = song3
# song3.next = song4
# song4.next = song2

# print(loop_length(song1))

# q6
# want to find the nodes that are either greater than their neighbours or less than
# cant be head or tail nodes

# p
# def func
#   set prev to head
#   set curr to head next
#   set count to 0
#   iterate while curr next not none
#       check if prev value less than curr value and curr next less than curr
#           increment count   

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

def count_critical_points(song_audio):
    pass