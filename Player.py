
class Player:
    
    def __init__(self, name, hidden_word=None, old_guesses=None, points=int):
        self.name = name
        self.hidden_word = hidden_word
        self.old_guesses = old_guesses
        self.points = points

    
    def add_point(self):
        self.points += 1
        return self.points

def get_players():
    """
    Creates and returns a list of Player objects based on user input for the number of players.
    
    :return: A list of Player objects.
    """
    num_players = int(input("Enter the number of players: "))
    players = []
    for i in range(num_players):
        player_name = input(f"Player {i + 1}: ")
        players.append(Player(player_name, points=0))
    return players
