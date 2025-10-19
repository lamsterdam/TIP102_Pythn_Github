# q1
# u
# want a function that maps each artists to the set time at the same index as that artist

# p
# def func
#   create a dictionary
#   iterate through both
#       add the elem from artist as the key and set the val to the elem at that index in set times
#   return the dictionary   

# i
# def lineup(artists, set_times):
#     lineupDict = {}
#     for i in range(len(artists)):
#         lineupDict[artists[i]] = set_times[i]
#     return lineupDict

# artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
# set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

# artists2 = []
# set_times2 = []

# print(lineup(artists1, set_times1))
# print(lineup(artists2, set_times2))

# q2
# u
# want a function that returns the value of the artist passed in if it exsists in the dictionary, if it doesnt exist return the default dictionary

# p
# def func
#   check if the artist is in dictionary
#       if so return the value
#   otherwise
#       return {'message': 'Artist not found'}

# i
# def get_artist_info(artist, festival_schedule):
#     if artist in festival_schedule:
#         return festival_schedule[artist]
#     else:
#         return {'message': 'Artist not found'}

# festival_schedule = {
#     "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
#     "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
#     "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
#     "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
# }

# print(get_artist_info("Blood Orange", festival_schedule)) 
# print(get_artist_info("Taylor Swift", festival_schedule)) 

# q3
# u
# want a function that returns the sum of all the values in a dictionary

# p
# def func
#   get the values as a list from the dictionary
#   calculate the sum of the list of values
#   return the sum

# i
# def total_sales(ticket_sales):
#     listValues = ticket_sales.values()
#     sumOfValues = sum(listValues)
#     return sumOfValues

# ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

# print(total_sales(ticket_sales))

# q4
# u
# wnat to check two dictionaries for key value pairs that are the same, if same put them in a new dictionary and return

# p
# def func
#   create new dict
#   iterate through venue1 to create list of tuples using .items()
#       check if key and value is in venue2 and its the same
#           add it to the new dict
#   return new dict

# i
# def identify_conflicts(venue1_schedule, venue2_schedule):
#     newDict = {}
#     for key,value in venue1_schedule.items():
#         if key in venue2_schedule and venue2_schedule[key] == value:
#             newDict[key] = value
#     return newDict

# venue1_schedule = {
#     "Stromae": "9:00 PM",
#     "Janelle Monáe": "8:00 PM",
#     "HARDY": "7:00 PM",
#     "Bruce Springsteen": "6:00 PM"
# }

# venue2_schedule = {
#     "Stromae": "9:00 PM",
#     "Janelle Monáe": "10:30 PM",
#     "HARDY": "7:00 PM",
#     "Wizkid": "6:00 PM"
# }

# print(identify_conflicts(venue1_schedule, venue2_schedule))

# q5
# u
# want a func that returns the artist name that appears the most, if there is a ties just return of the the most frequent ones

# p
# def func
#   set maxVote to zero
#   set maxArtits to ""
#   use counter from collections function and pass in the votes values
#   iterate through key, val in the new dictionary
#       compare the value to maxVote
#           if greater update maxVote 
#           and update maxArtist
#   return maxArtist        

# i
# from collections import Counter
# def best_set(votes):
#     maxVote = 0
#     maxArtist = ""
#     newDict = Counter(votes.values())
#     for key,val in newDict.items():
#         if val > maxVote:
#             maxVote = val
#             maxArtist = key
#     return maxArtist

# votes1 = {
#     1234: "SZA", 
#     1235: "Yo-Yo Ma",
#     1236: "Ethel Cain",
#     1237: "Ethel Cain",
#     1238: "SZA",
#     1239: "SZA"
# }

# votes2 = {
#     1234: "SZA", 
#     1235: "Yo-Yo Ma",
#     1236: "Ethel Cain",
#     1237: "Ethel Cain",
#     1238: "SZA"
# }

# print(best_set(votes1))
# print(best_set(votes2))

# q6
# u
# want a function that takes in an array of integers and finds the largest number and retunrs
# that number, if that largests number appears more than once return the sum of them

# p
# def func
#   find the max and save it in a var
#   create a dictionary
#   iterate through the array
#       if elem equals the max
#           check if it is in the dictionary
#               if  so increase the count
#           otherwise
#               add it to the dictionary with a count of 1
#   return the max number * the value in dictionary

# i
# def max_audience_performances(audiences):
#     max_val = max(audiences)
#     myDict = {}
#     for each in audiences:
#         if each == max_val:
#             if each in myDict:
#                 myDict[each] += 1
#             else:
#                 myDict[each] = 1
#     return max_val * myDict[max_val]

# audiences1 = [100, 200, 200, 150, 100, 250]
# audiences2 = [120, 180, 220, 150, 220]

# print(max_audience_performances(audiences1))
# print(max_audience_performances(audiences2))

# q7
# u
# want a function that does the same as the previous function but don't use a dictionary
# this time, compare which one is better and why

# p
# def func
#   get the max value of the array and save in a var
#   create counter and set to 0
#   iterate through the array
#       check if elem is equal to max val
#           if so increase the count
#   return max value * count


# i
# def max_audience_performances(audiences):
#     max_val = max(audiences)
#     my_count = 0
#     for each in audiences:
#         if each == max_val:
#             my_count += 1
#     return max_val * my_count

# audiences1 = [100, 200, 200, 150, 100, 250]
# audiences2 = [120, 180, 220, 150, 220]

# print(max_audience_performances(audiences1))
# print(max_audience_performances(audiences2))

# the previous solution ran in O(n) time and used a hashmap which could be at most o(n) large
# if each val in the array was the max, this one also runs in O(n) but uses no extra space
# so this one is better

# q8
# u
# want a function that checks how many pairs af numbers have the same values, and second 
# cannot be in the same index as the first number, alos given the formula 
# number of pairs = (n x n-1)/2, where n is the number that appears more than once

# p
# def func
#   create a dictionary
#   iterate through the array
#       check if elem in dictionary
#           if so increase count
#       otherwise add to the dictionary
#   set num_pairs to zero
#  iterate for val in dict
#       check if key has val > 1
#           curr_pairs = (val * val-1) // 2 -> floor division to get an integer not a float
#           num_pairs += curr_pairs
#   return num_pairs


# i
# def num_popular_pairs(popularity_scores):
#     myDict = {}
#     for each in popularity_scores:
#         if each in myDict:
#             myDict[each] += 1
#         else:
#             myDict[each] = 1
#     num_pairs = 0
#     for val in myDict.values():
#         if val > 1:
#             curr_pairs = (val * (val-1)) // 2
#             num_pairs += curr_pairs
#     return num_pairs

# popularity_scores1 = [1, 2, 3, 1, 1, 3]
# popularity_scores2 = [1, 1, 1, 1]
# popularity_scores3 = [1, 2, 3]

# print(num_popular_pairs(popularity_scores1))
# print(num_popular_pairs(popularity_scores2))
# print(num_popular_pairs(popularity_scores3)) 

# q9
# u
# want a function that takes in two lists of strings and finds the abs diff in terms of index
# between the performers with the same name in both lists. Then sums this number and returns
# t is a permutation of s so all elem in s will appear in t, and at most once too

# p
# def func
#   create sDict
#   create tDict
#   iterate through s array
#       add elem to dict with index as the value
#   iterate through t array
#       add elem to dict with index as the value
#   total_sum = 0
#   iterate through keys in sDict
#       curr_diff = abs(sDict[value] - tDict[value])
#       total_sum += curr_diff
#   return total_sum

# i
def find_stage_arrangement_difference(s, t):
    """
    :type s: List[str]
    :type t: List[str]
    :rtype: int
    """
    
    