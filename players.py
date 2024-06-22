
class Player:
    name = ""
    hidden_word = ""
    old_guesses = []
    score_by_game = 0
    points = 0
    
        
    def add_score(self):
        self.score_by_game += 1
        return self.sscore_by_game
    
    def add_point(self):
        self.points += 1
        return self.points

list1 = [[1, 2], 2]
list2 = list1[:]
list1[0][0] = 5
print(list1, id(list1[0]))
print(list2, id(list2[0]))