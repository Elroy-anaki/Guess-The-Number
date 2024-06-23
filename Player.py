
class Player:
    
    def __init__(self, name, hidden_word=None, old_guesses=None, score_by_game=None, points=int):
        self.name = name
        self.hidden_word = hidden_word
        self.old_guesses = old_guesses
        self.score_by_game = score_by_game
        self.points = points

        
    def add_score(self):
        self.score_by_game += 1
        return self.sscore_by_game
    
    def add_point(self):
        self.points += 1
        return self.points
