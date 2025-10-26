# q1
# u
# want a function that uses the Player class and takes in a list of opponent player objects to return the player's place overall in the tournament

# p
# def func
#   create empty array
#   get the average of player's race outcomes list
#   append tuple of avg, player character to array
#   iterate through opponents list
#       get the average of each oponents race outcomes list
#       


# i
class Player:
    def __init__(self, character, kart, outcomes):
        self.character = character
        self.kart = kart
        self.outcomes = outcomes
    
    def get_tournament_place(self, opponents):
        player_avg = sum(self.outcomes) / len(self.outcomes)
        # op1_avg = sum(op)